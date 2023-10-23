import csv
from abc import ABC, abstractmethod

from .connect import PostgreSQLConnector


class AbstractExtractor(ABC):

    @abstractmethod
    def extract(self):
        pass


class PostgresExtractor(AbstractExtractor):
    def __init__(self, connection_details, query):
        self.connector = PostgreSQLConnector(**connection_details)
        self.query = query

    def extract(self):
        try:
            self.connector.connect()
            with self.connector.connection.cursor() as cur:
                cur.execute(self.query)
                result = cur.fetchall()
                column_names = [col[0] for col in cur.description]

                return column_names, result
        finally:
            self.connector.close()


class CSVExtractor(AbstractExtractor):
    def __init__(self, file_path):
        self.file_path = file_path

    def extract(self):
        data = []
        with open(self.file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                data.append(row)
        column_names = data[0]
        data = data[1:]
        return column_names, data
