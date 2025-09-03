import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS test (
        id INTEGER,
        name TEXT
    )
''')

cursor.execute('''
    INSERT INTO test
    VALUES (1, "Alice")
''')

conn.commit()

cursor.execute('''
    SELECT * FROM test
''')

for row in cursor.fetchall():
    print(row)

conn.close()
