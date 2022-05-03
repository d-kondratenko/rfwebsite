import hashlib


def create_hash(email, password):
    email = hashlib.md5(email.encode())
    password = hashlib.md5(password.encode())

    result = email.hexdigest() + password.hexdigest()

    return result
