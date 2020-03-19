from .extensions import db


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payer_email = db.Column(db.String(100))
    unix = db.Column(db.String(100))
    payment_date = db.Column(db.String(400))
    username = db.Column(db.String(400))
    last_name = db.Column(db.String(400))
    payment_gross = db.Column(db.Float(6,2))
    payment_fee = db.Column(db.Float(6,2))
    payment_net = db.Column(db.Float(6,2))
    payment_status = db.Column(db.String(400))
    txn_id = db.Column(db.String(100))

   

    def __repr__(self):
        return f"Reply('{self.username}', '{self.last_name}')"