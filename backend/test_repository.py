# Force all models to register
import models

from database.connection import SessionLocal
from repositories.contract_repository import ContractRepository

db = SessionLocal()

try:
    repo = ContractRepository(db)

    contract = repo.get_by_number("AZ-2026-001")

    if contract:
        print("Provider:", contract.provider)
        print("Service:", contract.service_name)
    else:
        print("Contract not found.")

finally:
    db.close()