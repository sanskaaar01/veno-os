from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Command(Base):
    __tablename__ = "commands"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String)
    command_text = Column(String)
    status = Column(String, default="pending")  # pending or executed
    timestamp = Column(DateTime, default=datetime.utcnow)