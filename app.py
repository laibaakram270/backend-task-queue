from fastapi import FastAPI, Depends
from database import SessionLocal, Job
import worker

app = FastAPI()

@app.on_event("startup")
def startup_event():
    worker.start_workers()  # workers only start when app starts

@app.post("/add-job")
def add_job(task_name: str, priority: str = "NORMAL"):
    db = SessionLocal()
    job = Job(task_name=task_name, priority=priority)
    db.add(job)
    db.commit()
    return {"id": job.id, "status": "Job Added"}

@app.get("/job/{job_id}")
def get_job(job_id: int):
    db = SessionLocal()
    job = db.query(Job).filter(Job.id==job_id).first()
    return job