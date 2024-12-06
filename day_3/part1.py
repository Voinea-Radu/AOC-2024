import re
from os.path import split


def process(data: str):
    result = 0

    regex = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    matches = re.findall(regex, data)
    for match in matches:
        terms = match[4:-1].split(",")
        result += int(terms[0]) * int(terms[1])

    print(result)
