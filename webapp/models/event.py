from webapp.extensions import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    txn_id = db.Column(db.String(25), nullable=False)
    amount = db.Column(db.Integer, default=0)
    event_type = db.Column(db.String(25), nullable=False)
    event_time = db.Column(db.Integer, default=-1)
    card_id = db.Column(db.ForeignKey("card.id"))
    card = db.relationship("Card", back_populates="events")

