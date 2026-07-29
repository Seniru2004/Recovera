from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

from sqlalchemy import Enum
from models.enums import IncidentSeverity, IncidentStatus

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    contract_id = Column(Integer, ForeignKey("contracts.id"), nullable=False)

    incident_code = Column(String)

    title = Column(String)

    severity = Column(
    Enum(IncidentSeverity)
)

    status = Column(
    Enum(IncidentStatus)
)

    description = Column(Text)

    

    opened_at = Column(DateTime)

    resolved_at = Column(DateTime)

    contract = relationship("Contract", back_populates="incidents")

    