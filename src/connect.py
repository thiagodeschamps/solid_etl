import psycopg2
import sqlite3
from abc import ABC


class AbstractConnector(ABC):
    ...


class PostgreSQLConnector(AbstractConnector):
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to PostgreSQL")
        except psycopg2.Error as e:
            print("Error connecting to PostgreSQL: %s", e)

    def close(self):
        if self.connection:
            self.connection.close()
            print("Closed PostgreSQL connection")


class SQLiteConnector(AbstractConnector):
    def __init__(self, database_path):
        self.database_path = database_path
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database_path)
            print("Connected to SQLite database")
        except sqlite3.Error as e:
            print("Error connecting to SQLite database:", e)

    def close(self):
        if self.connection:
            self.connection.commit()
            self.connection.close()
