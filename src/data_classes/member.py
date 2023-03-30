from src.data_classes.data_class import DataClass
from src.data_classes.group import Group
from src.utils.constants import data_path


class Member(DataClass):
    def __init__(self):
        super().__init__()
        self.id: int = None
        self.name: str = None
        self.wish: str = None
        self.recipient: Member = None
        self.group: Group = None

        self.data_table = data_path / "member.csv"

    def from_dict(self, dictionary):
        self.name = dictionary['name']
        self.wish = dictionary['wish']
        self.recipient = self.get_by_id(dictionary['recipient_id'])

        self.group = Group()
        self.group = self.group.get_by_id(dictionary['group_id'])

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'wish': self.wish,
            'recipient_id': self.recipient.id,
            'group_id': self.group.id
        }
