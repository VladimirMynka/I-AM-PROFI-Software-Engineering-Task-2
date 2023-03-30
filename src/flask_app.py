from flask import Flask, request, abort

from src.services.group_service import GroupService

app = Flask(__name__)


@app.post("/group")
def add_group():
    body = request.json
    if "name" not in body:
        abort(400)
    if "description" not in body:
        body["description"] = ""

    return GroupService.add_group(body)


@app.get("/groups")
def get_groups():
    return GroupService.get_all_groups()


@app.get("/group/<int:id_>")
def get_group(id_: int):
    response = GroupService.get_one_group(id_)
    if response is None:
        abort(404)
    return response


@app.put("/group/<int:id_>")
def put_group(id_: int):
    body = request.json
    if ("name" not in body) or (not isinstance(body["name"], str)):
        abort(400)
    response = GroupService.put_group(id_, body)
    if response is None:
        abort(404)

    return response


@app.delete("/group/<int:id_>")
def delete_group(id_: int):
    response = GroupService.delete_group(id_)
    if response is None:
        abort(404)

    return response


@app.post("/group/<int:id_>/participant")
def add_participant(id_: int):
    body = request.json
    response = GroupService.new_participant(id_, body)
    if response is None:
        abort(404)

    return response


@app.delete("/group/<int:id_>/participant/<int:participant_id>")
def delete_participant(id_: int, participant_id: int):
    response = GroupService.delete_participant(id_, participant_id)
    if response is None:
        abort(404)
    if isinstance(response, str):
        abort(int(response))
    return response


@app.post("/group/<int:id_>/toss")
def toss(id_: int):
    response = GroupService.toss(id_)
    if response is None:
        abort(404)
    if isinstance(response, int):
        abort(response)
    return response


@app.get("/group/<int:group_id>/participant/<int:participant_id>/recipient")
def get_recipient(group_id: int, participant_id: int):
    response = GroupService.get_recipient(group_id, participant_id)
    if response is None:
        abort(404)
    if isinstance(response, int):
        abort(response)
    return response


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
