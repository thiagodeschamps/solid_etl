from src.config import Config
from src.etl import ETL

# Configuration
config = Config(
    extractor_type="PostgresExtractor",
    loader_type="PandasToCSVLoader",
    transformers=["CursorToPandasTransformer"],
    extractor={
        "connection_details": {
            "host": "localhost",
            "database": "world",
            "user": "postgres",
            "password": "postgres"
        },
        "query": "SELECT * FROM public.city limit 10"
    },
    loader={
        "file_name": "output.csv"
    }
)

# ETL Process
etl_process = ETL(config)
etl_process.process()
