def print_disk(disk: list):
    for char in disk:
        print(char, end="")
    print()


def find_free_space(disk: list, last_one:int = None):
    if last_one is None:
        last_one = 0

    for index in range(last_one, len(disk)):
        if disk[index] == ".":
            return index


def find_last_bit(disk: list, last_one:int = None):
    if last_one is None:
        last_one = len(disk) - 1

    for index in range(last_one, -1, -1):
        if disk[index] != ".":
            return index


def compress_disk(disk: list):
    free_index = find_free_space(disk)
    last_bit = None

    while free_index != -1:
        last_bit = find_last_bit(disk, last_bit)

        print(f"{free_index}/{len(disk)}")

        # print(f"{free_index=}")
        # print(f"{last_bit=}")

        if last_bit == -1:
            break

        if last_bit < free_index:
            break

        disk[free_index] = disk[last_bit]
        disk[last_bit] = "."
        free_index = find_free_space(disk, free_index)

        # print_disk(disk)


def process(data_str: str):
    free_space: bool = False
    disk: list = []
    next_id: int = 0

    for char in data_str:
        if free_space:
            disk += ["."] * int(char)
        else:
            disk += [next_id] * int(char)
            next_id += 1
        free_space = not free_space

    print_disk(disk)
    compress_disk(disk)

    result = 0

    for index in range(len(disk)):
        if disk[index] == ".":
            break

        result += index * disk[index]

    print(result)
