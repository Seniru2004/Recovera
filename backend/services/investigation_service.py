from datetime import datetime

from services.sla_service import SLAService
from services.recovery_service import RecoveryService

from repositories.contract_repository import ContractRepository
from repositories.monitoring_repository import MonitoringRepository
from repositories.incident_repository import IncidentRepository
from repositories.email_repository import EmailRepository
from repositories.invoice_repository import InvoiceRepository

from repositories.evidence_repository import EvidenceRepository
from repositories.recovery_repository import RecoveryRepository
from repositories.audit_repository import AuditRepository

from models.user import User
from models.investigation import Investigation
from models.recovery_case import RecoveryCase
from models.audit_log import AuditLog

from models.enums import InvestigationStatus


class InvestigationService:

    def __init__(self, db):

        self.db = db

        # Repositories
        self.contract_repo = ContractRepository(db)
        self.monitoring_repo = MonitoringRepository(db)
        self.incident_repo = IncidentRepository(db)
        self.email_repo = EmailRepository(db)
        self.invoice_repo = InvoiceRepository(db)

        self.evidence_repo = EvidenceRepository(db)
        self.recovery_repo = RecoveryRepository(db)
        self.audit_repo = AuditRepository(db)

        # Services
        self.sla_service = SLAService()
        self.recovery_service = RecoveryService()

    def investigate(self, contract_id: int):

        # ---------------------------------
        # Load Contract
        # ---------------------------------

        contract = self.contract_repo.get_by_id(contract_id)

        if not contract:
            raise Exception("Contract not found")

        # ---------------------------------
        # Find System User
        # ---------------------------------

        system_user = (
            self.db.query(User)
            .filter(User.email == "admin@recovera.ai")
            .first()
        )

        if not system_user:
            raise Exception(
                "System administrator not found. Run database.seed first."
            )

        # ---------------------------------
        # Create Investigation
        # ---------------------------------

        investigation = Investigation(
            contract_id=contract.id,
            created_by=system_user.id,
            status=InvestigationStatus.RUNNING,
            confidence_score=0.95,
            started_at=datetime.utcnow(),
        )

        self.db.add(investigation)
        self.db.flush()

        # ---------------------------------
        # Load Related Data
        # ---------------------------------

        monitoring_logs = self.monitoring_repo.get_by_contract(contract.id)
        incidents = self.incident_repo.get_by_contract(contract.id)
        emails = self.email_repo.get_by_contract(contract.id)
        invoices = self.invoice_repo.get_by_contract(contract.id)

        if not monitoring_logs:
            raise Exception("No monitoring data found")

        if not invoices:
            raise Exception("No invoice data found")

        # ---------------------------------
        # Latest Records
        # ---------------------------------

        latest_monitoring = monitoring_logs[-1]
        latest_invoice = invoices[-1]

        # ---------------------------------
        # SLA Analysis
        # ---------------------------------

        sla_result = self.sla_service.check_breach(
            contract.guaranteed_uptime,
            latest_monitoring.uptime_percentage,
        )

        # ---------------------------------
        # Recovery Calculation
        # ---------------------------------

        eligible = self.recovery_service.check_eligibility(
            sla_result["breach"]
        )

        estimated_credit = (
            self.recovery_service.calculate_credit(
                latest_invoice.amount,
                contract.credit_percentage,
            )
            if eligible
            else 0
        )

        # ---------------------------------
        # Save Recovery Case
        # ---------------------------------

        recovery_case = RecoveryCase(
            investigation_id=investigation.id,
            eligible=eligible,
            estimated_credit=estimated_credit,
            justification=(
                "SLA breached based on monitoring logs."
                if eligible
                else "No SLA breach detected."
            ),
            created_at=datetime.utcnow(),
        )

        self.db.add(recovery_case)

        # ---------------------------------
        # Save Audit Log
        # ---------------------------------

        audit_log = AuditLog(
            user_id=system_user.id,
            action="Investigation Completed",
            details=(
                f"Investigation #{investigation.id} completed "
                f"for contract {contract.contract_number}."
            ),
            created_at=datetime.utcnow(),
        )

        self.db.add(audit_log)

        # ---------------------------------
        # Complete Investigation
        # ---------------------------------

        investigation.status = InvestigationStatus.COMPLETED
        investigation.completed_at = datetime.utcnow()

        self.db.commit()

        # ---------------------------------
        # Investigation Report
        # ---------------------------------

        report = {
            "investigation_id": investigation.id,
            "contract_number": contract.contract_number,
            "service": contract.service_name,
            "provider": contract.provider,
            "customer": contract.customer,
            "required_uptime": contract.guaranteed_uptime,
            "actual_uptime": latest_monitoring.uptime_percentage,
            "uptime_difference": sla_result["uptime_difference"],
            "sla_breach": sla_result["breach"],
            "incident_count": len(incidents),
            "email_count": len(emails),
            "invoice_amount": latest_invoice.amount,
            "estimated_credit": estimated_credit,
            "eligible": eligible,
        }

        return report