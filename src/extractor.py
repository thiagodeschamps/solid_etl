from abc import ABC, abstractmethod


class AbstractExtractor(ABC):

    @abstractmethod
    def extract(self):
        pass


class PostgresExtractor(AbstractExtractor):
    def __init__(self, connector, query):
        self.connector = connector
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
