import redis
from typing import Optional, List, Dict, Any
from rq import Queue
from rq.job import Job
from app.config import settings

_redis = redis.from_url(settings.redis_url)
q = Queue(name=settings.queue_name, connection=_redis)

def enqueue_reasoning(messages: List[Dict[str, Any]]) -> str:
    from app.reasoning_task import run_reasoning
    job = q.enqueue(
        run_reasoning, 
        messages, 
        job_timeout=420, # 7 minutes
        ttl=600, # 10 minutes
        result_ttl=600 # 10 minutes
        )
    
    return job

def get_job(job_id:str) -> Job:
    return Job.fetch(job_id, connection=_redis)