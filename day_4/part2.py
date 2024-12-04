SEARCH_DOMAIN = [
    [
        ["M", ".", "S"],
        [".", "A", "."],
        ["M", ".", "S"]
    ],
    [
        ["M", ".", "M"],
        [".", "A", "."],
        ["S", ".", "S"]
    ],
    [
        ["S", ".", "M"],
        [".", "A", "."],
        ["S", ".", "M"]
    ],
    [
        ["S", ".", "S"],
        [".", "A", "."],
        ["M", ".", "M"]
    ],
]

string_to_find: str = "XMAS"


def walkthrough(matrix: list[list[chr]], start_x: int, start_y: int) -> int:
    result: int = 0

    for direction in SEARCH_DOMAIN:
        x: int = start_x
        y: int = start_y
        found: bool = True

        for offset_y in range(len(direction)):
            for offset_x in range(len(direction[offset_y])):
                if x + offset_x >= len(matrix) or y + offset_y >= len(matrix[0]):
                    found = False
                    break

                if direction[offset_y][offset_x] == ".":
                    continue

                if matrix[y + offset_y][x + offset_x] != direction[offset_y][offset_x]:
                    found = False
                    break

            if not found:
                break

        if found:
            result += 1

    return result


def print_matrix(matrix: list[list[chr]]):
    print()

    for line in matrix:
        print(" ".join(line))

    print()


def process(data: str):
    char_matrix: list[list[chr]] = [list(line) for line in data.splitlines()]

    result: int = 0

    for y in range(len(char_matrix)):
        for x in range(len(char_matrix[y])):
            result += walkthrough(char_matrix, x, y)

    print(result)
