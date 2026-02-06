from fastapi import FastAPI
from app.services.workflow import run_workflow

app = FastAPI(title="Fulfillment Automation System")

@app.get("/")
def health_check():
    return {"status": "running"}

    @app.post("/run")
    def run():
        run_workflow()
            return {"message": "Workflow executed"}