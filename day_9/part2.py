class Block:
    size: int
    data: int

    def __init__(self, size: int, data: int):
        self.size = size
        self.data = data


def print_disk(disk: list):
    for block in disk:
        print(f"({block.size} x {block.data}) ", end="")
    print()

def print_disk_explicit(disk: list):
    for block in disk:
        data = str(block.data)
        if block.data == -1:
            data = "."

        print(data * block.size, end="")
    print()



def find_free_space(disk: list[Block], size: int) -> int:
    for index in range(0, len(disk)):
        if disk[index].data == -1 and disk[index].size >= size:
            return index

def compress_disk(disk: list):
    # print_disk(disk)
    # print_disk_explicit(disk)
    while True:
        found = False
        for last_block_index in range(len(disk) - 1, -1, -1):
            if disk[last_block_index].data != -1:
                free_index = find_free_space(disk, disk[last_block_index].size)
                # print(f"{last_block_index=}, {free_index=}")

                if free_index is None:
                    continue

                if last_block_index < free_index:
                    continue

                print(f"{free_index}/{len(disk)} || {last_block_index}/{len(disk)}")
                remaining_space =disk[free_index].size - disk[last_block_index].size
                disk[free_index].size = disk[last_block_index].size
                disk[free_index].data = disk[last_block_index].data

                disk[last_block_index].data = -1

                disk.insert(free_index + 1, Block(remaining_space, -1))
                found = True
                break

        if not found:
            break


def process(data_str: str):
    free_space: bool = False
    disk: list[Block] = []
    next_id: int = 0

    for char in data_str:
        if free_space:
            disk.append(Block(int(char), -1))
        else:
            disk.append(Block(int(char), next_id))
            next_id += 1

        free_space = not free_space

    # print_disk(disk)
    compress_disk(disk)

    result = 0
    counter = 0

    for block in disk:
        if block.data == -1:
            counter += block.size
            continue

        for _ in range(block.size):
            result += counter * block.data
            counter+=1


    print(result)
