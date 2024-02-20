from src.connection.base import Base
from src.entities.companies import Companies
from src.entities.patients import Patients
from src.entities.type_exams_aso import TypeExamsAso
from sqlalchemy import Column, String, DateTime, Integer, Numeric, ForeignKey
from datetime import datetime


class Forms(Base):
    __tablename__ = "forms"

    id = Column(String(256), primary_key=True)
    id_type_exam = Column(String(256), ForeignKey(TypeExamsAso.id, onupdate='CASCADE', ondelete='CASCADE'))
    id_company = Column(String(256), ForeignKey(Companies.id, onupdate='CASCADE', ondelete='CASCADE'))
    name_company = Column(String(256), nullable=False)
    id_patient = Column(String(256), ForeignKey(Patients.id, onupdate='CASCADE', ondelete='CASCADE'))
    name_patient = Column(String(256), nullable=False)
    rg = Column(String(256), nullable=False, unique=True)
    cnpj = Column(String(256), nullable=False, unique=True)
    cpf = Column(String(256), unique=True)
    function_patient = Column(String(256), nullable=False)
    number_procedures = Column(Integer, nullable=False)
    status_exam = Column(Integer, nullable=False)
    amount = Column(Numeric(precision=10, scale=2))
    comments = Column(String(256))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)


