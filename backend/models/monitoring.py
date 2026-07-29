from sqlalchemy import (
    Column,
    Integer,
    Float,
    DateTime,
    ForeignKey,
    String
)

from sqlalchemy.orm import relationship

from models.base import Base


class MonitoringLog(Base):
    __tablename__ = "monitoring_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    contract_id = Column(
        Integer,
        ForeignKey("contracts.id"),
        nullable=False
    )

    uptime_percentage = Column(
        Float,
        nullable=False
    )

    outage_minutes = Column(
        Integer
    )

    outage_start = Column(
        DateTime
    )

    outage_end = Column(
        DateTime
    )

    source = Column(
        String
    )

    contract = relationship(
        "Contract",
        back_populates="monitoring_logs"
    )