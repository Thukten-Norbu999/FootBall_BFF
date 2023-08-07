import sqlite3
import hashlib

class MatchData:
    def __init__(self, id, Category, HomeTeam, AwayTeam, matchDate, time):
        self.id_data = f'{HomeTeam} vs {AwayTeam} + {Category}'.encode('utf-8')
        self.id = hashlib.sha256(self.id_data).hexdigest()
        self.category = Category
        self.Hteam = HomeTeam
        self.Ateam = AwayTeam

        self.matchDate = matchDate
        self.time = time

        self.done = False

    
    def validate(self):
        if self.id not in None:
            pass


    def save(self):
        pass


