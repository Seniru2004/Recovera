import models

from sqlalchemy.orm import Session

from models.user import User
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db, User)

    def get_by_email(self, email: str):
        return (
            self.db.query(User)
            .filter(
                User.email == email
            )
            .first()
        )