from ast import literal_eval

from src.data_classes.data_class import DataClass
from src.data_classes.member import Member
from src.utils.constants import data_path


class Group(DataClass):
    def __init__(self):
        super().__init__()
        self.id: int = None
        self.name: str = None
        self.description: str = None
        self.participants: list[Member] = None

        self.data_table = data_path / "group.csv"
        self.converters = {
            'participants_ids': literal_eval
        }

    def from_dict(self, dictionary):
        self.name = dictionary['name']
        self.description = dictionary['description']

        self.participants = []
        for i in dictionary['participants_ids']:
            self.participants.append(Member().get_by_id(i))

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'participants_ids': [i.id for i in self.participants]
        }
