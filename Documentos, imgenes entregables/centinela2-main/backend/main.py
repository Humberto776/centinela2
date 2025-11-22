from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/v1/info")
def info():
    return {"service": "centinela-backend", "version": "0.1.0"}
