import random
import string

ALPHANUMERIC_CHAR = string.ascii_lowercase + string.digits
STRING_LENGTH = 6


def generate_random_string(chars=ALPHANUMERIC_CHAR, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))
