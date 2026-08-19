import time, random, threading
from database import SessionLocal, Job

MAX_RETRIES = 3

def process_job(job):
    print(f"Processing Job {job.id}: {job.task_name}")
    time.sleep(2)
    if random.random() < 0.3:
        raise Exception("Job failed")

def worker():
    db = SessionLocal()
    while True:
        job = db.query(Job).filter(Job.status=="PENDING").order_by(
            Job.priority.desc()
        ).first()
        if job:
            job.status = "RUNNING"
            db.commit()
            try:
                process_job(job)
                job.status = "DONE"
            except:
                job.retry_count += 1
                if job.retry_count >= MAX_RETRIES:
                    job.status = "DLQ"
                else:
                    job.status = "PENDING"
                    time.sleep(2**job.retry_count + random.random())
            db.commit()
        time.sleep(1)

def start_workers():
    for i in range(3):
        threading.Thread(target=worker, daemon=True).start()