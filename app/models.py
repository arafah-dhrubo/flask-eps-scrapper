from app import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(4))
    month = db.Column(db.String(2))
    eps = db.Column(db.String(6))

    def __repr__(self):
        return self.eps