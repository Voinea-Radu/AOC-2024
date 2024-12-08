class Position:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.y}, {self.x})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class PositionPair:
    pos1: Position
    pos2: Position

    def __init__(self, pos1: Position, pos2: Position):
        self.pos1 = pos1
        self.pos2 = pos2

    def __str__(self):
        return f"({self.pos1}, {self.pos2})"

    def __eq__(self, other):
        return (self.pos1 == other.pos1 and self.pos2 == other.pos2) or \
            (self.pos1 == other.pos2 and self.pos2 == other.pos1)


def print_map(char_map: list[list[chr]]):
    print()
    for line in char_map:
        print("".join(line))


def get_pairs(char_map: list[list[chr]]) -> list[PositionPair]:
    pairs: list[PositionPair] = []

    size = len(char_map)

    for y1 in range(size):
        for x1 in range(size):
            if char_map[y1][x1] != ".":
                for y2 in range(size):
                    for x2 in range(size):
                        if char_map[y2][x2] == char_map[y1][x1] and (x1 != x2 or y1 != y2):
                            pairs.append(PositionPair(Position(x1, y1), Position(x2, y2)))

    result = []

    for pair in pairs:
        if pair not in result:
            result.append(pair)

    return result


def process_pairs(pairs: list[PositionPair], anti_node_map: list[list[chr]]):
    size = len(anti_node_map)
    for position_pair in pairs:
        pos1 = position_pair.pos1
        pos2 = position_pair.pos2

        diff_x = pos2.x - pos1.x
        diff_y = pos2.y - pos1.y

        anti_node_1_x = pos1.x - diff_x
        anti_node_1_y = pos1.y - diff_y

        anti_node_2_x = pos2.x + diff_x
        anti_node_2_y = pos2.y + diff_y

        if 0 <= anti_node_1_x < size and 0 <= anti_node_1_y < size:
            print(f"[1] ({pos1},{pos2}) => {Position(pos1.x - diff_x, pos1.y - diff_y)}")
            anti_node_map[pos1.y - diff_y][pos1.x - diff_x] = "#"

        if 0 <= anti_node_2_x < size and 0 <= anti_node_2_y < size:
            print(f"[2] ({pos1},{pos2}) => {Position(anti_node_2_x, anti_node_2_y)}")
            anti_node_map[anti_node_2_y][anti_node_2_x] = "#"


def process(data: str):
    char_map: list[list[chr]] = [list(line) for line in data.splitlines()]
    anti_node_map: list[list[chr]] = [["." for _ in range(len(char_map[0]))] for _ in range(len(char_map))]

    pairs: list[PositionPair] = get_pairs(char_map)
    for position_pair in pairs:
        print(position_pair)

    print(len(pairs))
    process_pairs(pairs, anti_node_map)

    print_map(char_map)
    print_map(anti_node_map)

    print(sum([line.count("#") for line in anti_node_map]))
