from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from your real FastAPI server!"}
"""FastAPI Backend — Inventory Management API"""

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/health")
def health_check():
    try:
        # Simulate a database connection check here
        # If this check fails, it will jump to the except block
        
        return {"status": "healthy", "service": "inventory-api"}
    except Exception:
        # Return a 503 Service Unavailable error when the connection fails
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection failed"
        )
