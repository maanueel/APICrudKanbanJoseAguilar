from sqlalchemy import Column, Integer, String
from database import Base

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, default="pendiente")  # Ej: pendiente, en_progreso, completada
    assignee = Column(String)  # Persona asignada