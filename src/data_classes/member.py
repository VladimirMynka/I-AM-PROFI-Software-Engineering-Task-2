from src.data_classes.data_class import DataClass
from src.utils.constants import data_path


class Member(DataClass):
    def __init__(self):
        super().__init__()
        self.id: int = None
        self.name: str = None
        self.wish: str = None
        self.recipient: Member = None

        self.data_table = data_path / "member.csv"

    def get_by_recipient(self, recipient_id):
        table = self.read()
        return table[table["recipient_id"] == recipient_id].index.tolist()

    def from_dict(self, dictionary, count_of_recurs=5):
        self.name = dictionary['name']
        self.wish = dictionary['wish']

        if count_of_recurs > 0:
            self.recipient = self.get_by_id(dictionary['recipient_id'], count_of_recurs-1)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'wish': self.wish,
            'recipient_id': self.recipient.id if self.recipient is not None else None,
        }
