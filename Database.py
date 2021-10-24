# Database

import sqlite3

db = sqlite3.connect("app.db")

db.execute("CREATE TABLE skills (name text, progress integer, user_id integer)")
