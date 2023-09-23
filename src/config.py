class Config:
    def __init__(self, extractor_type, loader_type, transformers=None, **kwargs):
        self.extractor_type = extractor_type
        self.loader_type = loader_type
        self.transformers = transformers or []
        self.kwargs = kwargs

    def get_class_reference(self, module, class_name):
        return getattr(module, class_name)

    def get_extractor_config(self):
        return self.kwargs.get("extractor", {})

    def get_loader_config(self):
        return self.kwargs.get("loader", {})

    def get_transformer_configs(self):
        return self.transformers
