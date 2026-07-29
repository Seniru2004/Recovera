from datetime import datetime, date
import traceback

from database.connection import SessionLocal

from models.contract import Contract
from models.monitoring import MonitoringLog
from models.incident import Incident
from models.email import Email
from models.invoice import Invoice
from models.user import User

from models.enums import (
    UserRole,
    ContractStatus,
    IncidentSeverity,
    IncidentStatus,
    EmailType,
)

db = SessionLocal()

try:

    # =========================================================
    # USER
    # =========================================================

    user = (
        db.query(User)
        .filter(User.email == "admin@recovera.ai")
        .first()
    )

    if not user:

        user = User(
            name="System Administrator",
            email="admin@recovera.ai",
            role=UserRole.ADMIN,
            company="RECOVERA",
        )

        db.add(user)
        db.flush()

        print("✅ Demo user created.")

    # =========================================================
    # CONTRACT
    # =========================================================

    contract = (
        db.query(Contract)
        .filter(Contract.contract_number == "AZ-2026-001")
        .first()
    )

    if not contract:

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
        db.flush()

        print("✅ Contract created.")

    # =========================================================
    # MONITORING
    # =========================================================

    monitoring = (
        db.query(MonitoringLog)
        .filter(MonitoringLog.contract_id == contract.id)
        .first()
    )

    if not monitoring:

        monitoring = MonitoringLog(
            contract_id=contract.id,
            uptime_percentage=99.72,
            outage_minutes=168,
            outage_start=datetime(2026, 7, 15, 10, 30),
            outage_end=datetime(2026, 7, 15, 13, 18),
            source="Azure Monitor",
        )

        db.add(monitoring)

        print("✅ Monitoring log created.")

    # =========================================================
    # INCIDENT
    # =========================================================

    incident = (
        db.query(Incident)
        .filter(Incident.incident_code == "INC-2026-001")
        .first()
    )

    if not incident:

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

        print("✅ Incident created.")

    # =========================================================
    # EMAIL
    # =========================================================

    email = (
        db.query(Email)
        .filter(Email.subject == "Azure Service Incident Notification")
        .first()
    )

    if not email:

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

        print("✅ Email created.")

    # =========================================================
    # INVOICE
    # =========================================================

    invoice = (
        db.query(Invoice)
        .filter(Invoice.invoice_number == "INV-2026-0701")
        .first()
    )

    if not invoice:

        invoice = Invoice(
            contract_id=contract.id,
            invoice_number="INV-2026-0701",
            amount=50000,
            billing_month="July 2026",
            issue_date=date(2026, 7, 1),
            paid=True,
        )

        db.add(invoice)

        print("✅ Invoice created.")

    # =========================================================
    # COMMIT
    # =========================================================

    db.commit()

    print("\n🎉 Database seeding completed successfully!")

except Exception:

    db.rollback()
    traceback.print_exc()

finally:

    db.close()