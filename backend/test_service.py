import models

from database.connection import SessionLocal

from services.investigation_service import InvestigationService


db = SessionLocal()

try:

    service = InvestigationService(db)

    report = service.investigate(1)

    print("\n========== RECOVERA REPORT ==========\n")

    for key, value in report.items():
        print(f"{key}: {value}")

finally:
    db.close()