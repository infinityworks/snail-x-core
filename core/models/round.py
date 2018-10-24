from core import db

class Round(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)

    def __init__(self, id, name, start_date, end_date):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return "<Round\nid: {}\n name: {}\n start_date: {}>".format(self.id, self.name, self.start_date)

    def get_round(self, id):
        return self.query.filter_by(id=id).first()

    def get_all_rounds(self):
        return self.query.all()