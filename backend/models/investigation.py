from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
    Enum,
)
from sqlalchemy.orm import relationship

from models.base import Base
from models.enums import InvestigationStatus


class Investigation(Base):
    __tablename__ = "investigations"

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

    created_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    status = Column(
        Enum(InvestigationStatus),
        default=InvestigationStatus.RUNNING,
        nullable=False
    )

    confidence_score = Column(
        Float,
        default=0.0,
        nullable=False
    )

    final_decision = Column(
        String
    )

    started_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    completed_at = Column(
        DateTime
    )

    # Relationships

    contract = relationship(
        "Contract",
        back_populates="investigations"
    )

    user = relationship(
        "User",
        back_populates="investigations"
    )

    evidence = relationship(
        "Evidence",
        back_populates="investigation",
        cascade="all, delete-orphan"
    )

    recovery_case = relationship(
        "RecoveryCase",
        back_populates="investigation",
        uselist=False,
        cascade="all, delete-orphan"
    )