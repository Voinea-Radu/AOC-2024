def blink(row: dict[int, int]) -> dict[int, int]:
    new_row:dict[int, int] = {}

    for stone in row.keys():
        stones_count = row[stone]

        if stone == 0:
            if 1 not in new_row:
                new_row[1] = stones_count
            else:
                new_row[1] += stones_count
            continue

        stone_len = len(str(stone))

        if stone_len % 2 == 0:
            big_10 = (10 ** (stone_len // 2))
            left  = stone // big_10
            right = stone % big_10

            if left not in new_row:
                new_row[left] = stones_count
            else:
                new_row[left] += stones_count

            if right not in new_row:
                new_row[right] = stones_count
            else:
                new_row[right] += stones_count

            continue

        new_stone = stone * 2024

        if new_stone not in new_row:
            new_row[new_stone] = stones_count
        else:
            new_row[new_stone] += stones_count

    return new_row


def process(data: str):
    row: list[int] = [int(number_str) for number_str in data.split(" ")]
    row_dict:dict[int, int] = {}

    for stone in row:
        if stone not in row_dict:
            row_dict[stone] = 1
        else:
            row_dict[stone] += 1

    for i in range(0, 75):
        print(f"{i}/75")
        row_dict = blink(row_dict)

    result = 0

    for stone in row_dict.keys():
        result += row_dict[stone]

    print(result)
