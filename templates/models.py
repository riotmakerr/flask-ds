from application import db

class results(db.Model):
    idresults = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(75))
    leave_chance = db.Column(db.FLOAT)

    def __init__(self, name, chance):
        self.employee_name = name
        self.leave_chance = chance

    # def __repr__(self):
    #     return '<Data %r>' % self.notes
