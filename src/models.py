from sqlalchemy import Column, Integer, Float, DateTime
from database import Base
import datetime


class Historial(Base):
    __tablename__ = "historial_conversiones"

    id = Column(Integer, primary_key=True, index=True)
    monto_origen = Column(Float, nullable=False)
    monto_resultado = Column(Float, nullable=False)
    fecha = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<Conversion(id={self.id}, monto={self.monto_origen})>"
