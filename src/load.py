import sqlite3
from abc import ABC, abstractmethod


class AbstractLoader(ABC):
    @abstractmethod
    def load(self, data):
        pass


class PandasToCSVLoader(AbstractLoader):
    def __init__(self, file_name):
        self.file_name = file_name

    def load(self, data):
        data.to_csv(self.file_name)


class PandasToSQLiteLoader(AbstractLoader):
    def __init__(self, connector, table_name):
        self.connector = connector
        self.table_name = table_name

    def load(self, data):
        try:
            self.connector.connect()
            data.to_sql(self.table_name, self.connector.connection, if_exists='replace', index=False)
            print(f"Data loaded into SQLite table '{self.table_name}'")
        except Exception as e:
            print("Error loading data into SQLite:", e)
        finally:
            self.connector.close()
