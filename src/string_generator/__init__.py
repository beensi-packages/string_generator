import uuid
import hashlib


def uuid_maker():
    return f'{uuid.uuid4().hex}{uuid.uuid4().hex}'[:63]


def hashed_password(value: str):
    return hashlib.sha512(value.encode()).hexdigest()
