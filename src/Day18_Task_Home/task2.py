import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# 1️⃣ Create interns table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    intern_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# 2️⃣ Create mentors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mentor_name TEXT,
    track TEXT
)
""")

# 3️⃣ Insert sample data ONLY if tables are empty
cursor.execute("SELECT COUNT(*) FROM interns")
if cursor.fetchone()[0] == 0:
    cursor.executemany("""
    INSERT INTO interns (name, track, stipend)
    VALUES (?, ?, ?)
    """, [
        ("Amit", "Data Science", 6000),
        ("Rahul", "Data Science", 7000),
        ("Neha", "Web Dev", 4500),
        ("Karan", "Web Dev", 5000),
        ("Priya", "AI", 8000)
    ])

cursor.execute("SELECT COUNT(*) FROM mentors")
if cursor.fetchone()[0] == 0:
    cursor.executemany("""
    INSERT INTO mentors (mentor_name, track)
    VALUES (?, ?)
    """, [
        ("Dr. Sharma", "Data Science"),
        ("Ms. Iyer", "Web Dev"),
        ("Mr. Verma", "AI")
    ])

conn.commit()

# 4️⃣ INNER JOIN: Interns with their track mentor
join_query = """
SELECT 
    i.name AS intern_name,
    i.track,
    m.mentor_name
FROM interns i
INNER JOIN mentors m
ON i.track = m.track
"""

df_joined = pd.read_sql_query(join_query, conn)

# 5️⃣ Display result
print("=== Interns with Their Mentors ===")
print(df_joined)

conn.close()