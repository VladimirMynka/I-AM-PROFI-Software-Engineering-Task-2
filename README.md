# I-AM-PROFI-Software-Engineering-Task-2

### python version: 3.10

## Flask Application (Without docker)

- Rename data/group_scheme.csv and data/member_scheme.csv to data/group.csv and data/member.csv
- `pip install -r requirements.txt` - to install requirements
- `nohup python -m src.flask_app &` - to run application

## Docker

- `docker-compose run --build -d`

## API Description

#### API Endpoints

###### POST `/group`
- Request body: [PostPutGroup](#PostPutGroup)
- Response: int - id of created group
- Errors:
  - 400 - "name" is not in body


###### GET `/groups`
- Response: List<[GroupCommonInformation](#GroupCommonInformation)>

###### GET `/group/{id}`
- Response: [GroupFullInformation](#GroupFullInformation)
- Errors:
  - 404 - group with id {id} didn't find

###### PUT `/group/{id}`
- Request body: [PostPutGroup](#PostPutGroup)
- Response: [GroupCommonInformation](#GroupCommonInformation)
- Errors:
  - 404 - group with id {id} didn't find

###### DELETE `/group/{id}`
- Response: int - id of deleted group
- Errors:
  - 404 - group with id {id} didn't find

###### POST `/group/{id}/participant`
- Request body: [PostMember](#PostMember)
- Response: int - id of created member
- Errors:
  - 404 - group with id {id} didn't find
  - 400 - "name" is not in body

###### DELETE `/group/{groupId}/participant/{participantId}`
- Response: int - id of deleted member
- Errors:
  - 404 - group with id {id} didn't find or member with id {participantId} didn't find
  - 403 - user can be deleted because he is recipient of another user

###### POST `/group/{id}/toss`
- Response: List<[MemberWithRecipient](#MemberWithRecipient)> of deleted member
- Errors:
  - 404 - group with id {id} didn't find
  - 409 - not enough members

###### GET `/group/{groupId}/participant/{participantId}/recipient`
- Response: List<[MemberCommonInformation](#MemberCommonInformation)> of deleted member
- Errors:
  - 404 - group or member with id didn't find
  - 409 - recipient is not defined

#### Schemes:

###### PostPutGroup:

```json
{
  "name": "string",
  "description": "string" // can be empty
}
```

###### GroupCommonInformation:

```json
{
  "id": 0,
  "name": "string",
  "description": "string"
}
```

###### MemberCommonInformation:
```json
{
  "id": 0,
  "name": "string",
  "wish": "string"
}
```

###### MemberWithRecipient:
```json
{
  "id": 0,
  "name": "string",
  "wish": "string",
  "recipient": MemberCommonInformation | null
}
```

###### GroupFullInformation:
```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "participants": [
    MemberWithRecipient,
    MemberWithRecipient,
    ...
    MemberWithRecipient
  ]
}
```

###### PostMember:
```json
{
  "name": "string",
  "wish": "string" // can be empty
}
```

