import random, string

def generate_random(stringLength: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation.replace("/", "").replace("?", "")
    return ''.join(random.choice(characters) for i in range(stringLength))