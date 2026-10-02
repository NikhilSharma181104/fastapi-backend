from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from your real FastAPI server!"}
"""FastAPI Backend — Inventory Management API"""

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/ping")
def ping():
    return {"message": "pong"}
