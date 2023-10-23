import pandas as pd
from abc import ABC, abstractmethod


class AbstractTransform(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def transform(self):
        pass


class CursorToPandasTransformer(AbstractTransform):
    def __init__(self, data):
        super().__init__(data)

    def transform(self):
        df = pd.DataFrame(self.data[1], columns=self.data[0])
        return df
