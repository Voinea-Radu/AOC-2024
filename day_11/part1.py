def blink(row:list[int]) -> list[int]:
    new_row = []
    for stone in row:
        if stone == 0:
            new_row.append(1)
            continue

        stone_len = len(str(stone))

        if stone_len % 2 == 0:
            big_10 = (10 ** (stone_len // 2))
            new_row.append(stone // big_10)
            new_row.append(stone % big_10)
            continue

        new_row.append(stone * 2024)

    return new_row

def process(data: str):
    row:list[int] = [int(number_str) for number_str in data.split(" ")]

    for i in range(0, 25):
        print(f"{i+1}/75")
        row = blink(row)

    print(len(row))
