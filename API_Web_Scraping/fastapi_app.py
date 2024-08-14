"""

"""

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Mock data to be returned by the API
mock_data = {"message": "This is protected data."}

# Simple OAuth2 token validation
def validate_token(token: str):
    valid_token = "your_access_token_here"
    if token == valid_token:
        return True
    return False

@app.get("/data")
async def get_data(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    token = authorization.split(" ")[1]
    if not validate_token(token):
        raise HTTPException(status_code=403, detail="Invalid token")

    return mock_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
