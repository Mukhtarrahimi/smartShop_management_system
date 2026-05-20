def validate_email(email):
    if "@" not in email or "." not in email:
        return False
    return True


def validate_password(password):
    if len(password) < 8:
        return False
    return True


def validate_name(name):
    if len(name.strip()) < 2:
        return False
    return True