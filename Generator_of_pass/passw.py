import secrets


def create_pass(length, characters):
    return ''.join(secrets.choice(characters) for _ in range(length))
