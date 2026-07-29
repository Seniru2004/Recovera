from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base
from sqlalchemy import Enum
from models.enums import EmailType

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)

    contract_id = Column(Integer, ForeignKey("contracts.id"), nullable=False)

    sender = Column(String)

    recipient = Column(String)

    subject = Column(String)

    body = Column(Text)

    sent_at = Column(DateTime)

    email_type = Column(
    Enum(EmailType)
)

    contract = relationship("Contract", back_populates="emails")