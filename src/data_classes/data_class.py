from pathlib import Path

import pandas as pd


class DataClass:
    def __init__(self):
        self.id: int = None
        self.data_table: Path = None
        self.converters: dict = None

    def save(self):
        table = pd.read_csv(self.data_table, index_col=0, converters=self.converters)
        table.loc[self.id] = self.to_dict()
        table.to_csv(self.data_table)

    def load(self, id_: int, dictionary: dict):
        self.id = id_
        self.from_dict(dictionary)
        return self

    def get_by_id(self, id_):
        table = pd.read_csv(self.data_table, index_col=0)
        dictionary = table.loc[id_].to_dict()
        return self.load(id_, dictionary)

    def from_dict(self, dictionary):
        pass

    def to_dict(self) -> dict:
        pass
