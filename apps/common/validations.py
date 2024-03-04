import re

email_regex = r'^([a-z0-9]+[.-_]*)*[a-z0-9]+@[a-z0-9-]+(\.[a-z0-9-]+)*\.[a-zA-Z]{2,}$'


def validate_email(email):
    if re.search(email_regex, email):
        return True
    else:
        return False
