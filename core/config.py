import os
from supabase import create_client
from openai import OpenAI

supabase = None
openai_client = None

def init_clients():
    global supabase, openai_client

    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")

    if supabase_url and supabase_key:
        supabase = create_client(supabase_url, supabase_key)

    if openai_key:
        openai_client = OpenAI(api_key=openai_key)

