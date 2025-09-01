from fastapi import FastAPI

app = FastAPI(title="Auth Microservice", version="0.1.0")


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "auth-microservice"}