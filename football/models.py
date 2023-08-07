##
import hashlib,uuid
##
from main import db


class Matches(db.Model):
    id = db.Column(db.String, primary_key=True, unique=True, default=str(uuid.uuid4()))
    homeTeam = db.Column(db.String(100), nullable=False)
    awayTeam = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(10000), nullable=False)
    id_code = f'{homeTeam} vs {awayTeam} - {category}'.encode('utf-8')
    identifier = db.Column(db.String(10000), unique=True)
    matchDate = db.Column(db.Date, nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'{self.homeTeam} vs {self.awayTeam} - {self.category}'