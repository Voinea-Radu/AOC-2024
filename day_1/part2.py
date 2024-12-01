def process(data: str):
    list_1: list[int] = [int(line.split("   ")[0]) for line in data.splitlines()]
    list_2: list[int] = [int(line.split("   ")[1]) for line in data.splitlines()]

    result:int = 0

    for elem in list_1:
        result += list_2.count(elem) * elem

    print(result)