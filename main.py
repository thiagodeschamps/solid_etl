from src.connect import PostgreSQLConnector, SQLiteConnector
from src.extractor import PostgresExtractor
from src.transform import CursorToPandasTransformer
from src.load import PandasToCSVLoader, PandasToSQLiteLoader
from src.etl import ETL

query = 'Select name, population from public.city limit 10'
sqlite_database_path = "your_database.db"
sqlite_output_table = "example_table"

postgres_connector = PostgreSQLConnector
    host='localhost',
    database='world',
    user='postgres',
    password='postgres'
)
sqlite_connector = SQLiteConnector(sqlite_database_path)

# Extract from Postgres -> Transform to a DataFrame -> Load to CSV
etl = ETL(
    extractor=PostgresExtractor(postgres_connector, query),
    transformer=CursorToPandasTransformer,
    loader=PandasToCSVLoader('output.csv')
)
etl.process()

# Extract from Postgres -> Transform to a DataFrame -> Load to SQLite
etl = ETL(
    extractor=PostgresExtractor(postgres_connector, query),
    transformer=CursorToPandasTransformer,
    loader=PandasToSQLiteLoader(sqlite_connector, sqlite_output_table)
)
etl.process()
