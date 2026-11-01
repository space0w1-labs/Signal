import sqlite3


def get_user(conn: sqlite3.Connection, username: str):
    query = f"SELECT * FROM users WHERE name = '{username}'"
    return conn.execute(query).fetchone()


def average(values):
    return sum(values) / len(values)
