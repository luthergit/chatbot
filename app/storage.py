import psycopg
import os
import time
from psycopg_pool import AsyncConnectionPool
from typing import Optional, List, Dict, Any

DB_URL = os.environ.get("DATABASE_URL")

_pool: Optional[AsyncConnectionPool] = None

async def init_db():
    global _pool
    if _pool is None:
        _pool = AsyncConnectionPool(DB_URL, min_size=1, max_size=5, open=False)
        await _pool.open()

    async with _pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id BIGSERIAL PRIMARY KEY,
                user_id TEXT NOT NULL,
                timestamp BIGINT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL
);

""")
            await cur.execute("CREATE INDEX IF NOT EXISTS idx_messages_user ON messages (user_id);")
        await conn.commit()

async def close_db():
    global _pool
    if _pool is not None:
        await _pool.close()
        _pool = None

async def save_message(user_id: str, role: str, content: str):

    if _pool is None:
        raise RuntimeError("Database not initialized")
    
    async with _pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute("""
                INSERT INTO messages (user_id, timestamp, role, content) 
                              VALUES (%s, %s, %s, %s)""",
                              (user_id, int(time.time()), role, content)
)
            # print(f"DB save -> user={user_id} role={role} len={len(content)}")
            await conn.commit()
            
async def load_messages(user_id: str, limit: int = 10) -> List[Dict[str, Any]]:
    if _pool is None:
        raise RuntimeError("Database not initialized")
    
    async with _pool.connection() as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT role, content FROM messages WHERE user_id = %s ORDER BY timestamp DESC LIMIT %s""",
                              (user_id, limit))
            rows = await cur.fetchall()

    rows.reverse()
    
    return [{"role": row[0], "content": row[1]} for row in rows]