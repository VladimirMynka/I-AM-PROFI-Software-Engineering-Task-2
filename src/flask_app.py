from flask import Flask, request

app = Flask(__name__)

@app.post("/group")
def add_group():
    body = request.json


@app.get("/groups")
def get_groups():
    args = request.args


@app.get("/group/<id>")
def get_groups():
    args = request.args


@app.put("/group/<id>")
def get_groups():
    args = request.args


@app.delete("/group/<id>")
def get_groups():
    args = request.args


@app.post("/group/<id>/participant")
def get_groups():
    args = request.args


@app.delete("/group/<id>/participant/<participant_id>")
def get_groups():
    args = request.args


@app.post("/group/<id>/toss")
def get_groups():
    args = request.args


@app.get("/group/{groupId}/participant/<participant_id>/recipient")
def get_groups():
    args = request.args


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
