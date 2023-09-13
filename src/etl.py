import logging

class ETL:
    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader
        self.logger = logging.getLogger("ETL")

    def process(self):
        try:
            data = self.extractor.extract()
            data = self.transformer(data).transform()
            self.loader.load(data)
        except Exception as e:
            raise e
        finally:
            print('done')