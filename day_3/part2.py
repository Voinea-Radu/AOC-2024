import re
from os.path import split


def process(data: str):
    result = 0

    regex = r"(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don't\(\))"
    matches = re.findall(regex, data)

    enabled = True
    for match in matches:
        mul, do, dont = match
        if do:
            enabled = True
        if dont:
            enabled = False

        if mul != "" and enabled:
            terms = mul[4:-1].split(",")
            result += int(terms[0]) * int(terms[1])

    print(result)
