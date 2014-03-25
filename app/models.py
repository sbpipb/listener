from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class Trends(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    keyword = db.Column(db.String(140))  
    woe_id = db.Column(db.Integer)
    woe_code = db.Column(db.String(6))
    timestamp = db.Column(db.DateTime)    

    def __repr__(self):
        return '<Post %r>' % (self.keyword)