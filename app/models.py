from app import db


class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trade_code = db.Column(db.String(15))

    def __repr__(self):
        return self.code


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trade_id = db.Column(db.Integer, db.ForeignKey('trade.id'))
    year = db.Column(db.String(10))
    month = db.Column(db.String(10))
    eps = db.Column(db.String(10))

    def __repr__(self):
        return self.eps
