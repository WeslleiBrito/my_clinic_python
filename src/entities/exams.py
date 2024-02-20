from src.connection.base import Base
from sqlalchemy import Column, String, DateTime, Numeric
from datetime import datetime


class Exams(Base):
    __tablename__ = "exams"

    id = Column(String(256), primary_key=True)
    name = Column(String(256), nullable=False)
    price = Column(Numeric(precision=10, scale=2))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
