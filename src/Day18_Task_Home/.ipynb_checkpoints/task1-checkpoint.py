import sqlite3
import pandas as pd

# Connect to database (creates file if missing)
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# 1️⃣ Create table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# 2️⃣ Insert data ONLY if table is empty
cursor.execute("SELECT COUNT(*) FROM interns")
count = cursor.fetchone()[0]

if count == 0:
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
    conn.commit()

# 3️⃣ Filter
df_filter = pd.read_sql_query("""
SELECT *
FROM interns
WHERE track = 'Data Science' AND stipend > 5000
""", conn)

# 4️⃣ Aggregate
df_avg = pd.read_sql_query("""
SELECT track, AVG(stipend) AS avg_stipend
FROM interns
GROUP BY track
""", conn)

# 5️⃣ Count
df_count = pd.read_sql_query("""
SELECT track, COUNT(*) AS total_interns
FROM interns
GROUP BY track
""", conn)

# Output
print("=== Filtered Interns ===")
print(df_filter)

print("\n=== Average Stipend per Track ===")
print(df_avg)

print("\n=== Intern Count per Track ===")
print(df_count)

conn.close()