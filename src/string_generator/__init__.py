import uuid
import hashlib
import json


def uuid_maker():
    return f'{uuid.uuid4().hex}{uuid.uuid4().hex}'[:63]


def hashed_password(value: str):
    return hashlib.sha512(value.encode()).hexdigest()


def hashed_data(value: dict):
    tmp = {}
    for k, v in value.items():
        tmp[k] = str(v)
    tmp = json.dumps(tmp)
    return hashlib.sha512(tmp.encode()).hexdigest()
