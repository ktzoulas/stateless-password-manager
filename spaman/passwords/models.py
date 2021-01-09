from spaman import db


class HashName(db.Model):
    __tablename__ = 'hash_name'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(8), nullable=False)

    def __init__(self, name):
        self.name = name
