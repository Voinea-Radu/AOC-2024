from ctypes import c_uint

directions = [
    (0, -1),  # N
    (1, 0),  # E
    (0, 1),  # S
    (-1, 0),  # W
]


def find_start(char_map: list[list[chr]]) -> tuple[int, int]:
    for y in range(len(char_map)):
        for x in range(len(char_map[y])):
            if char_map[y][x] == "^":
                return x, y


def check_position(x: int, y: int, char_map: list[list[chr]]) -> bool:
    if x < 0 or y < 0 or y >= len(char_map) or x >= len(char_map[0]):
        return False
    return True


def move(x: int, y: int, char_map: list[list[chr]], visited_map: list[list[list[int]]], direction: int) -> bool:
    """
    :return: True if the path is circular and False if it is not
    """
    while True:
        if direction in visited_map[y][x]:
            return True

        visited_map[y][x].append(direction)

        offset_x = directions[direction][0]
        offset_y = directions[direction][1]

        if not check_position(x + offset_x, y + offset_y, char_map):
            return False

        while char_map[y + offset_y][x + offset_x] == "#":
            direction = (direction + 1) % len(directions)
            offset_x = directions[direction][0]
            offset_y = directions[direction][1]

            if not check_position(x + offset_x, y + offset_y, char_map):
                return False

        x = x + offset_x
        y = y + offset_y


def print_matrix(matrix: list[list[chr]]):
    print()
    print()
    for row in matrix:
        print("".join(row))

def print_visited(matrix: list[list[list[int]]]):
    print()
    print()
    for row in matrix:
        for cell in row:
            print(f"{str(cell):8}", end=" ")
        print()

def process(data: str):
    char_map: list[list[chr]] = [list(line) for line in data.splitlines()]

    x, y = find_start(char_map)
    result = 0

    total = len(char_map) * len(char_map[0])
    current = 0

    for obstacle_y in range(len(char_map)):
        for obstacle_x in range(len(char_map[obstacle_y])):
            current +=1

            if current % 1000 == 0:
                print(f"{current}/{total}")

            if char_map[obstacle_y][obstacle_x] != ".":
                continue

            visited_map = [[[] for _ in line] for line in char_map]
            char_map[obstacle_y][obstacle_x] = "#"

            if move(x, y, char_map, visited_map, 0):
                result += 1

            char_map[obstacle_y][obstacle_x] = "."



    print(result)
