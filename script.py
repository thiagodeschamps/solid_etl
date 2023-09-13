from src.connect import PostgreSQLConnector, SQLiteConnector
from src.extractor import PostgresExtractor
from src.transform import CursorToPandasTransformer
from src.load import PandasToSQLiteLoader
from src.etl import ETL

postgres_connector = PostgreSQLConnector(
                    host='localhost',
                    database='world',
                    user='postgres',
                    password='postgres'
                )

query = 'Select name, population from public.city limit 10'
database_path = "your_database.db"  # Replace with your SQLite database file path
table_name = "example_table2"

etl = ETL(
    extractor=PostgresExtractor(postgres_connector, query),
    transformer=CursorToPandasTransformer,
    loader=PandasToSQLiteLoader(SQLiteConnector(database_path), table_name)
)
etl.process()
