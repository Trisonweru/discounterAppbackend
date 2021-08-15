from Application import db

class DiscountCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    code = db.Column(db.String(100))

    def __repr__(self):
        return '<DiscountCode %r>' % self.title

db.create_all()
