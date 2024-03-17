import sqlite3

conn = sqlite3.connect('nou3.db')

c = conn.cursor()

#c.execute("""CREATE TABLE web (
 #   id integer PRIMARY KEY,
  #  first_name text,
   # last_name text,
    #email text,
    #firm text,
    #domain text,
    #message text
    #)""")

c.execute("SELECT * FROM web")

rows = c.fetchall()


for row in rows:
    print(row)

conn.commit()

conn.close()