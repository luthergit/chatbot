from dotenv import load_dotenv
load_dotenv()

from langfuse import Langfuse, observe, get_client
from langfuse.langchain import CallbackHandler

langfuse = get_client()
lf_handler = CallbackHandler()