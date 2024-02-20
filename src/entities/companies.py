from src.connection.base import Base
from sqlalchemy import Column, String, DateTime
from datetime import datetime


class Companies(Base):
    __tablename__ = "companies"

    id = Column(String(256), primary_key=True)
    name = Column(String(256), nullable=False)
    cnpj = Column(String(256), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __init__(self, id: str, name: str, cnpj: str, created_at: datetime = datetime.now(), updated_at: datetime = datetime.now()):
        self.id = id
        self.name = name
        self.cnpj = cnpj,
        self.created_at = created_at
        self.updated_at = updated_at


