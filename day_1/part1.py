def process(data: str):
    list_1: list[int] = [int(line.split("   ")[0]) for line in data.splitlines()]
    list_2: list[int] = [int(line.split("   ")[1]) for line in data.splitlines()]

    result:int = 0
    entries_count:int = len(list_1)

    for _ in range(entries_count):
        min_1:int = min(list_1)
        min_2:int = min(list_2)

        result += abs(min_2-min_1)

        list_1.remove(min_1)
        list_2.remove(min_2)

    print(result)