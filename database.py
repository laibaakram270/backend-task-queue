from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime

Base = declarative_base()
engine = create_engine("sqlite:///./jobs.db")
SessionLocal = sessionmaker(bind=engine)

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String)
    priority = Column(String)  # CRITICAL, HIGH, NORMAL, LOW
    status = Column(String, default="PENDING")  # PENDING, RUNNING, DONE, FAILED, DLQ
    retry_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(bind=engine)