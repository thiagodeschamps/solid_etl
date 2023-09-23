from . import extractor
from . import transform
from . import load


class ETL:
    def __init__(self, config):
        self.config = config
        self.extractor = self._get_instance(extractor, self.config.extractor_type, self.config.get_extractor_config())
        self.transformers = [self._get_instance(transform, t) for t in self.config.get_transformer_configs()]
        self.loader = self._get_instance(load, self.config.loader_type, self.config.get_loader_config())

    def _get_instance(self, module, class_name, config=None):
        cls = self.config.get_class_reference(module, class_name)
        if config:
            return cls(**config)
        else:
            return cls

    def process(self):
        # Extract
        data = self.extractor.extract()

        # Transform
        for transformer in self.transformers:
            data = transformer.transform(data)

        # Load
        self.loader.load(data)

        print("ETL process completed successfully!")
