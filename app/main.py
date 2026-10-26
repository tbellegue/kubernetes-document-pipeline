from fastapi import FastAPI

app = FastAPI(title="Kubernetes Document Pipeline - Milestone 1")

@app.get("/")
def root():
    return {"message": "Kubernetes Document Pipeline starter is running."}

@app.get("/health")
def health():
    return {"status": "ok"}