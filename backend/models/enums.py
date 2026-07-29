from enum import Enum


class InvestigationStatus(str, Enum):
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"


class IncidentSeverity(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class IncidentStatus(str, Enum):
    OPEN = "Open"
    INVESTIGATING = "Investigating"
    RESOLVED = "Resolved"


class UserRole(str, Enum):
    ADMIN = "Admin"
    ANALYST = "Analyst"
    CLIENT = "Client"


class EvidenceSource(str, Enum):
    CONTRACT = "Contract"
    MONITORING = "Monitoring"
    INCIDENT = "Incident"
    EMAIL = "Email"
    INVOICE = "Invoice"
    AI_ANALYSIS = "AI Analysis"


class EmailType(str, Enum):
    NOTIFICATION = "Notification"
    SUPPORT = "Support"
    ACKNOWLEDGEMENT = "Acknowledgement"

class ContractStatus(str, Enum):
    ACTIVE = "Active"
    EXPIRED = "Expired"
    TERMINATED = "Terminated"