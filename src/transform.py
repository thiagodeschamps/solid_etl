from abc import ABC

import pandas as pd


class AbstractTransform(ABC):
    def __init__(self, data):
        self.data = data

    def transform(self):
        pass


class CursorToPandasTransformer(AbstractTransform):
    def __init__(self, data):
        super().__init__(data)

    def transform(self):
        df = pd.DataFrame(self[1], columns=self[0])
        return df
