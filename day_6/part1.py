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


def move(x: int, y: int, char_map: list[list[chr]], visited_map: list[list[bool]], direction: int):
    while True:
        visited_map[y][x] = "X"

        offset_x = directions[direction][0]
        offset_y = directions[direction][1]

        if not check_position(x + offset_x, y + offset_y, char_map):
            return

        while char_map[y + offset_y][x + offset_x] == "#":
            direction += 1
            direction %= len(directions)
            offset_x = directions[direction][0]
            offset_y = directions[direction][1]

            if not check_position(x + offset_x, y + offset_y, char_map):
                return

        x = x + offset_x
        y = y +offset_y


def print_matrix(matrix: list[list[chr]]):
    print()
    print()
    for row in matrix:
        print("".join(row))


def process(data: str):
    char_map: list[list[chr]] = [list(line) for line in data.splitlines()]
    visited_map: list[list[chr]] = [[char for char in line] for line in char_map]
    print_matrix(char_map)

    x, y = find_start(char_map)

    move(x, y, char_map, visited_map, 0)
    print_matrix(visited_map)

    print(sum([line.count("X") for line in visited_map]))
