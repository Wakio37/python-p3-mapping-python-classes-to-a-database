import sqlite3

CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()

# CURSOR.execute('''
#     CREATE TABLE IF NOT EXISTS songs (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         album TEXT
#     )
# ''')

# CURSOR.execute("INSERT INTO songs (name, album) VALUES (?, ?)", ("Blinding Lights", "After Hours"))

# CURSOR.execute("SELECT * FROM songs")
# rows = CURSOR.fetchall()
# for row in rows:
#     print(row)
# CONN.commit()



