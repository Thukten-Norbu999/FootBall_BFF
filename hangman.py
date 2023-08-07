
import sqlite3
import hashlib
print(hashlib.sha256('transportunitedfc vs parofc'.encode('utf-8')).hexdigest()==hashlib.sha256('transportunitedfc vs parofc'.encode('utf-8')).hexdigest())
print(hashlib.sha256('parofc vs transportunitedfc'.encode('utf-8')).hexdigest()==hashlib.sha256('transportunitedfcvs parofc'.encode('utf-8')).hexdigest())
print("x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z" == "x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z")

con = sqlite3.connect("C:/Users/Kinga Norbu/Desktop/game/data/database.db")
cur = con.cursor()

username = 'Thukten Norbu'
cur.execute("SELECT id, dob FROM User WHERE name = ?", (username,))
row = cur.fetchone()

if row is not None:
    user_id = row[0]
    age = row[1]
    print(user_id, age)
else:
    print('Nothing')