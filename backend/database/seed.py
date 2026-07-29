from datetime import datetime, date

from database.connection import SessionLocal

from models.contract import Contract
from models.monitoring import MonitoringLog
from models.incident import Incident
from models.email import Email
from models.invoice import Invoice

from models.user import User
from models.investigation import Investigation
from models.evidence import Evidence
from models.recovery_case import RecoveryCase
from models.audit_log import AuditLog

from models.user import User
from models.enums import UserRole

from models.enums import (
    ContractStatus,
    IncidentSeverity,
    IncidentStatus,
    EmailType,
)

import traceback


db = SessionLocal()

try:

    # ---------------------------------------------------------
    # Check whether the database has already been seeded
    # ---------------------------------------------------------

    existing = (
        db.query(Contract)
        .filter(Contract.contract_number == "AZ-2026-001")
        .first()
    )

    if existing:
        print("Database already seeded.")
        exit()

    # ---------------------------------------------------------
    # Contract
    # ---------------------------------------------------------

    contract = Contract(
        contract_number="AZ-2026-001",
        provider="Microsoft Azure",
        customer="ABC Technologies",
        service_name="Azure SQL Database",
        guaranteed_uptime=99.9,
        credit_percentage=10,
        start_date=date(2026, 1, 1),
        end_date=date(2026, 12, 31),
        status=ContractStatus.ACTIVE,
    )

    db.add(contract)

    # Generates contract.id without committing
    db.flush()

    # ---------------------------------------------------------
    # Monitoring Log
    # ---------------------------------------------------------

    monitoring = MonitoringLog(
        contract_id=contract.id,
        uptime_percentage=99.72,
        outage_minutes=168,
        outage_start=datetime(2026, 7, 15, 10, 30),
        outage_end=datetime(2026, 7, 15, 13, 18),
        source="Azure Monitor",
    )

    db.add(monitoring)

    # ---------------------------------------------------------
    # Incident
    # ---------------------------------------------------------

    incident = Incident(
        contract_id=contract.id,
        incident_code="INC-2026-001",
        title="Azure SQL Database Outage",
        severity=IncidentSeverity.HIGH,
        description=(
            "Azure SQL Database became unavailable due to a "
            "regional infrastructure issue."
        ),
        status=IncidentStatus.RESOLVED,
        opened_at=datetime(2026, 7, 15, 10, 30),
        resolved_at=datetime(2026, 7, 15, 13, 18),
    )

    db.add(incident)

    # ---------------------------------------------------------
    # Email
    # ---------------------------------------------------------

    email = Email(
        contract_id=contract.id,
        sender="support@microsoft.com",
        recipient="it@abctech.com",
        subject="Azure Service Incident Notification",
        body=(
            "We have identified a service disruption affecting "
            "Azure SQL Database. Our engineering teams have "
            "mitigated the issue and service has been restored."
        ),
        sent_at=datetime(2026, 7, 15, 11, 5),
        email_type=EmailType.NOTIFICATION,
    )

    db.add(email)

    # ---------------------------------------------------------
    # Invoice
    # ---------------------------------------------------------

    invoice = Invoice(
        contract_id=contract.id,
        invoice_number="INV-2026-0701",
        amount=50000,
        billing_month="July 2026",
        issue_date=date(2026, 7, 1),
        paid=True,
    )

    db.add(invoice)

    # ---------------------------------------------------------
    # Commit Everything
    # ---------------------------------------------------------

    db.commit()

    print("✅ Database seeded successfully!")

except Exception:
    db.rollback()
    traceback.print_exc()

finally:

    db.close()