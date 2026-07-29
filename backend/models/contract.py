from sqlalchemy import Column, Integer, String, Float, Date, Enum
from sqlalchemy.orm import relationship

from models.base import Base
from models.enums import ContractStatus


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    contract_number = Column(
        String,
        unique=True,
        nullable=False
    )

    provider = Column(
        String,
        nullable=False
    )

    customer = Column(
        String,
        nullable=False
    )

    service_name = Column(
        String,
        nullable=False
    )

    guaranteed_uptime = Column(
        Float,
        nullable=False
    )

    credit_percentage = Column(
        Float,
        nullable=False
    )

    start_date = Column(
        Date
    )

    end_date = Column(
        Date
    )

    status = Column(
        Enum(ContractStatus),
        default=ContractStatus.ACTIVE,
        nullable=False
    )


    # Relationships

    investigations = relationship(
        "Investigation",
        back_populates="contract"
    )

    monitoring_logs = relationship(
        "MonitoringLog",
        back_populates="contract",
        cascade="all, delete-orphan"
    )

    incidents = relationship(
        "Incident",
        back_populates="contract",
        cascade="all, delete-orphan"
    )

    emails = relationship(
        "Email",
        back_populates="contract",
        cascade="all, delete-orphan"
    )

    invoices = relationship(
        "Invoice",
        back_populates="contract",
        cascade="all, delete-orphan"
    )