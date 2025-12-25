from fastapi import Header, HTTPException
from core.config import SERVICE_API_KEY

def verify_api_key(x_api_key: str = Header(...)):
    if SERVICE_API_KEY and x_api_key != SERVICE_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
