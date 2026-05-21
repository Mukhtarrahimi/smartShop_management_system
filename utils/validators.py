def validate_email(email):

    if "@" not in email or "." not in email:
        return False

    if (
        email.startswith('@') or
        email.startswith('.') or
        email.endswith('@') or
        email.endswith('.')
    ):
        return False

    return True


def validate_password(password):

    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False

    return True


def validate_name(name):

    name = name.strip()

    if len(name) < 2:
        return False

    if any(char.isdigit() for char in name):
        return False

    return True