from sqlalchemy.orm import Session


class BaseRepository:

    def __init__(self, db: Session, model):
        self.db = db
        self.model = model

    def get_by_id(self, obj_id: int):
        return (
            self.db.query(self.model)
            .filter(self.model.id == obj_id)
            .first()
        )

    def get_all(self):
        return self.db.query(self.model).all()

    def create(self, obj):
        self.db.add(obj)
        self.db.flush()      # <-- changed
        return obj

    def update(self):
        self.db.flush()

    def delete(self, obj):
        self.db.delete(obj)
        self.db.flush()