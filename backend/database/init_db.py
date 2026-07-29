from database.connection import engine
from models.base import Base
from models.monitoring import MonitoringLog
from models.incident import Incident
from models.email import Email
from models.invoice import Invoice
from models.user import User
from models.investigation import Investigation
from models.evidence import Evidence
from models.recovery_case import RecoveryCase
from models.audit_log import AuditLog

# Import every model so SQLAlchemy knows about them
from models.contract import Contract

Base.metadata.create_all(bind=engine)

print("✅ Database tables created successfully!")