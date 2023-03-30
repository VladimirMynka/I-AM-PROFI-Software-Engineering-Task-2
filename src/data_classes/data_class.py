from pathlib import Path

import pandas as pd


class DataClass:
    def __init__(self):
        self.id: int = None
        self.data_table: Path = None
        self.converters: dict = None

    def read(self) -> pd.DataFrame:
        return pd.read_csv(self.data_table, index_col=0, converters=self.converters)

    def save(self):
        if self.id is None:
            self.id = self.get_new_id()
        table = self.read()
        table.loc[self.id] = self.to_dict()
        table.to_csv(self.data_table)

    def load(self, id_: int | None, dictionary: dict, count_of_recurs=5):
        self.id = id_
        self.from_dict(dictionary, count_of_recurs)
        return self

    def delete(self):
        table = self.read()
        table = table[table.index != self.id]
        table.to_csv(self.data_table)

    def get_new_id(self):
        table = self.read()
        max_id = max(table.index)
        return max_id + 1

    def get_by_id(self, id_: int, count_of_recurs=5):
        if id_ is None:
            return None
        table = self.read()
        if id_ not in table.index:
            return None
        dictionary = table.loc[id_].to_dict()
        return self.load(id_, dictionary, count_of_recurs)

    def from_dict(self, dictionary, count_of_recurs=5):
        pass

    def to_dict(self) -> dict:
        pass

    def get_all(self) -> dict:
        return self.read().to_dict('index')
