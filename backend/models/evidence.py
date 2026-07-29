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
from models.enums import EvidenceSource


class Evidence(Base):
    __tablename__ = "evidence"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    investigation_id = Column(
        Integer,
        ForeignKey("investigations.id"),
        nullable=False
    )

    source_type = Column(
        Enum(EvidenceSource),
        nullable=False
    )

    # ID of the original record (contract, monitoring log, email, etc.)
    source_record_id = Column(
        Integer,
        nullable=False
    )

    # AI's conclusion from that record
    finding = Column(
        String,
        nullable=False
    )

    # Exact value or excerpt that supports the finding
    supporting_data = Column(
        String
    )

    # Confidence score (0–100 or 0.0–1.0, whichever you standardise on)
    confidence = Column(
        Float,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    investigation = relationship(
        "Investigation",
        back_populates="evidence"
    )