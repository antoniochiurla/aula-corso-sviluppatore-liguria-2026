import psycopg2
import os

print("Hello World from Python running inside a Docker container!")

try:
    conn = psycopg2.connect(
        host="database_dev",
        database="devdb",
        user="devuser",
        password="devpassword")
    print("Successfully connected to the PostgreSQL database!")
    conn.close()
    
except Exception as e:
    print(f"non potete andare in bagno, troppi caffè: {e}")