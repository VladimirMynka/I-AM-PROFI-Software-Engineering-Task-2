import random

from src.data_classes.group import Group
from src.data_classes.member import Member


class GroupService:
    @staticmethod
    def add_group(body: dict):
        group = Group()
        group.load(None, body)
        group.save()
        return group.id

    @staticmethod
    def get_all_groups():
        group = Group()
        all_data = group.get_all()
        result = [
            {
                "id": i,
                "name": all_data[i]["name"],
                "description": all_data[i]["description"]
            }
            for i in all_data
        ]
        return result

    @staticmethod
    def get_one_group(id_: int):
        group = Group()
        group = group.get_by_id(id_, count_of_recurs=2)
        if group is None:
            return None

        group_dict = group.to_dict()
        group_dict["participants"] = [Member().get_by_id(i, count_of_recurs=2) for i in group_dict["participants_ids"]]
        for participant in group_dict["participants"]:
            recipient = group_dict["participants"]["recipient_id"]
            if recipient is None:
                del(group_dict["participants"][participant]["recipient_id"])
                group_dict["participants"][participant]["recipient"] = None
                continue

            recipient = Member().get_by_id(
                group_dict["participants"]["recipient_id"],
                count_of_recurs=1
            )
            recipient = recipient.to_dict()
            del(recipient["recipient_id"])
            del(group_dict["participants"][participant]["recipient_id"])
            group_dict["participants"][participant]["recipient"] = recipient

        return group_dict

    @staticmethod
    def put_group(id_: int, body: dict):
        group = Group()
        group = group.get_by_id(id_, count_of_recurs=2)
        if group is None:
            return None

        if ("description" not in body) or (body["description"] is None):
            body["description"] = ""

        group.name = body["name"]
        group.description = body["description"]

        group.save()

        return group.get_by_id(id_, count_of_recurs=1).to_dict()

    @staticmethod
    def delete_group(id_: int):
        group = Group()
        group = group.get_by_id(id_, count_of_recurs=2)
        if group is None:
            return None

        group.delete()
        return id_

    @staticmethod
    def new_participant(group_id: int, body: dict):
        group = Group()
        group = group.get_by_id(group_id, count_of_recurs=2)
        if group is None:
            return None

        body["recipient_id"] = None
        member = Member().load(None, body, count_of_recurs=0)
        member.save()

        group.participants.append(member)
        group.save()

        return member.id

    @staticmethod
    def delete_participant(group_id: int, participant_id: int):
        group = Group().get_by_id(group_id, count_of_recurs=2)
        if group is None:
            return None

        member = Member().get_by_id(participant_id, count_of_recurs=2)
        if member is None:
            return None

        for_who_he_is_recipient = Member().get_by_recipient(member.id)
        if len(for_who_he_is_recipient) > 0:
            return "403"

        group.participants = [Member().get_by_id(i.id, 0) for i in group.participants if i.id != participant_id]
        group.save()

        member.delete()
        return participant_id

    @staticmethod
    def _toss_group(ids):
        while True:
            free = ids.copy()
            recipients = []
            for i in ids:
                available = [j for j in free if j != i]
                if len(available) == 0:
                    break
                chosen = random.choice(available)
                free.remove(chosen)
                recipients.append(chosen)
            if len(ids) == len(recipients):
                return recipients

    @staticmethod
    def toss(group_id: int):
        group = Group().get_by_id(group_id, count_of_recurs=2)
        if group is None:
            return None

        if len(group.participants) < 3:
            return 409

        ids = [i.id for i in group.participants]
        recipients = GroupService._toss_group(ids)

        for participant, choice in zip(group.participants, recipients):
            participant.recipient = Member().get_by_id(choice, 0)
            participant.save()

        return GroupService.get_one_group(group_id)["participants"]

    @staticmethod
    def get_recipient(group_id: int, participant_id: int):
        group = Group().get_by_id(group_id, count_of_recurs=2)
        if group is None:
            return None

        member = Member().get_by_id(participant_id, count_of_recurs=2)
        if member is None:
            return None

        if member.recipient is None:
            return 409

        res = member.to_dict()
        del(res["recipient_id"])

        return res
