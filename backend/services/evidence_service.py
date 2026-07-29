from datetime import datetime

from models.evidence import Evidence
from models.enums import EvidenceSource



class EvidenceService:


    def create_evidence(
        self,
        db,
        investigation_id,
        source,
        title,
        description,
        confidence
    ):


        evidence = Evidence(

            investigation_id=investigation_id,

            source_type=source,

            title=title,

            description=description,

            confidence=confidence,

            created_at=datetime.utcnow()
        )


        db.add(evidence)

        db.commit()

        db.refresh(evidence)


        return evidence