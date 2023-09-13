from abc import ABC

import pandas as pd


class AbstractTransform(ABC):
    def __init__(self, data):
        self.data = data

    def transform(self):
        pass


class CursorToPandasTransformer(AbstractTransform):
    def __init__(self, data):
        super().__init__(data=data)

    def transform(self):
        df = pd.DataFrame(self.data[1], columns=self.data[0])

        return df
