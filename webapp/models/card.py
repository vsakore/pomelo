from webapp import db


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    max_credit = db.Column(db.Integer, nullable=False)
    avl_credit = db.Column(db.Integer, nullable=False)
    payable_bal = db.Column(db.Integer, nullable=False)
    events = db.relationship("Event", back_populates="card")
