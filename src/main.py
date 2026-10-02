from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from your real FastAPI server!"}
"""FastAPI Backend — Inventory Management API"""

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "inventory-api"}
