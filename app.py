import httpx
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class UserData(BaseModel):
    name: str
    email: str
    stack: str


class ResponseModel(BaseModel):
    status: str = "success"
    user: UserData
    timestamp: str
    fact: str


@app.get("/me", response_model=ResponseModel)
async def get_profile():

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get("https://catfact.ninja/fact")
            response.raise_for_status()
            data = response.json()
            cat_fact = data["fact"]
    except Exception:
        cat_fact = "Couldn't fetch cat fact, try again"

    user = UserData(
        name="Mohamed Ali",
        email="mohamedcali@gmail.com",
        stack="Python/Fastapi",
    )

    return ResponseModel(
        user=user,
        timestamp=datetime.utcnow().isoformat() + "Z",
        fact=cat_fact
    )
