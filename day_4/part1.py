DIRECTIONS: list[tuple[int, int]] = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

string_to_find: str = "XMAS"

def walkthrough(matrix: list[list[chr]], start_x: int, start_y: int, found_matrix: list[list[chr]]) -> int:
    result: int = 0

    for direction in DIRECTIONS:
        x: int = start_x
        y: int = start_y
        found: bool = False
        search_string = string_to_find[1:]

        if matrix[y][x] != string_to_find[0]:
            continue

        for index, char in enumerate(search_string):
            x += direction[0]
            y += direction[1]

            if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
                break

            if matrix[y][x] != char:
                break

            if index == len(search_string) - 1:
                found = True
                break

        if found:
            x = start_x
            y = start_y

            found_matrix[y][x] = string_to_find[0]

            for index, char in enumerate(search_string):
                x += direction[0]
                y += direction[1]
                found_matrix[y][x] = char

            result += 1

    return result

def print_matrix(matrix: list[list[chr]]):
    print()

    for line in matrix:
        print(" ".join(line))

    print()

def process(data: str):
    char_matrix: list[list[chr]] = [list(line) for line in data.splitlines()]
    found_matrix: list[list[chr]] = [["."] * len(char_matrix[0]) for _ in range(len(char_matrix))]

    result: int = 0

    for y in range(len(char_matrix)):
        for x in range(len(char_matrix[y])):
            result += walkthrough(char_matrix, x, y,found_matrix)

    print(result)
