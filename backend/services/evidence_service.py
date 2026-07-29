from datetime import datetime
import json

from models.evidence import Evidence
from models.enums import EvidenceSource


class EvidenceService:

    def __init__(self, evidence_repo):
        self.evidence_repo = evidence_repo

    def generate(
        self,
        investigation_id,
        monitoring_logs,
        incidents,
        emails,
    ):

        evidences = []

        # ---------------------------------
        # Monitoring Evidence
        # ---------------------------------

        for monitoring in monitoring_logs:

            evidence = Evidence(
                investigation_id=investigation_id,
                source_type=EvidenceSource.MONITORING,
                source_record_id=monitoring.id,
                finding=(
                    f"Service uptime recorded at "
                    f"{monitoring.uptime_percentage}%."
                ),
                supporting_data=json.dumps({
                    "uptime_percentage": monitoring.uptime_percentage,
                    "outage_minutes": monitoring.outage_minutes,
                }),
                confidence=0.99,
                created_at=datetime.utcnow(),
            )

            self.evidence_repo.create(evidence)
            evidences.append(evidence)

        # ---------------------------------
        # Incident Evidence
        # ---------------------------------

        for incident in incidents:

            incident_data = {
                "description": incident.description,
            }

            if hasattr(incident, "severity"):
                incident_data["severity"] = (
                    incident.severity.value
                    if hasattr(incident.severity, "value")
                    else str(incident.severity)
                )

            if hasattr(incident, "status"):
                incident_data["status"] = (
                    incident.status.value
                    if hasattr(incident.status, "value")
                    else str(incident.status)
                )

            evidence = Evidence(
                investigation_id=investigation_id,
                source_type=EvidenceSource.INCIDENT,
                source_record_id=incident.id,
                finding=f"Incident detected: {incident.title}",
                supporting_data=json.dumps(incident_data),
                confidence=0.95,
                created_at=datetime.utcnow(),
            )

            self.evidence_repo.create(evidence)
            evidences.append(evidence)

        # ---------------------------------
        # Email Evidence
        # ---------------------------------

        for email in emails:

            evidence = Evidence(
                investigation_id=investigation_id,
                source_type=EvidenceSource.EMAIL,
                source_record_id=email.id,
                finding=(
                    f"Provider communication received: "
                    f"{email.subject}"
                ),
                supporting_data=json.dumps({
                    "subject": email.subject,
                    "body": email.body,
                }),
                confidence=0.90,
                created_at=datetime.utcnow(),
            )

            self.evidence_repo.create(evidence)
            evidences.append(evidence)

        return evidences