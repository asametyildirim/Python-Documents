import sqlite3

db = sqlite3.connect("project.db")

yetki= db.cursor()

yetki.execute("CREATE TABLE IF NOT EXISTS users (name,surname,age) ")
yetki.execute('INSERT INTO uyeler VALUES("samet","yildirim","23")')
db.commit()
db.close()