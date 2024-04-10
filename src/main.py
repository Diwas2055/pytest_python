# main.py

import uvicorn
from fastapi import FastAPI

app = FastAPI()

app.openapi_version = "3.0.2"


@app.get("/api/{s}")
async def homepage(s: int):
    return {"message": s * s}


@app.post("/api/echo")
async def echo(data: dict):
    return data


if __name__ == "__main__":
    uvicorn.run(app)
