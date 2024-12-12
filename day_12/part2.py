import math
from PIL import Image, ImageDraw

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_plot(garden: list[list[chr]], target_crop: chr, x: int, y: int) -> list[tuple[int, int]]:
    if garden[y][x] != target_crop:
        return []

    garden[y][x] = "#"

    plot = [(x, y)]

    for dx, dy in DIRECTIONS:
        new_x, new_y = x + dx, y + dy
        plot += get_plot(garden, target_crop, new_x, new_y)

    return plot


def get_area(garden: list[list[chr]], plot: list[tuple[int, int]]) -> int:
    return len(plot)


def find_close(garden: list[list[chr]], plot: list[tuple[int, int]], x: int, y: int, found: list[tuple[int, int]]):
    for check_x, check_y in plot:
        if abs(check_x - x) + abs(check_y - y) == 1:
            found.append((check_x, check_y))

    return x, y


class Side:
    x: int
    y: int
    side: tuple[int, int]

    def __init__(self, x: int, y: int, side: tuple[int, int]):
        self.x = x
        self.y = y
        self.side = side


def get_perimeter(garden: list[list[chr]], plot: list[tuple[int, int]]) -> int:
    # if len(plot) == 0:
    #     return 0

    # if len(plot) == 1:
    #     return 4

    #798595
    #798587

    corners_count = 0

    for x, y in plot:
        slot = garden[y][x]
        if garden[y + 1][x] != slot and garden[y][x + 1] != slot:
            print(f"Right outer bottom corner {x=} {y=}")
            corners_count += 1
        if  garden[y - 1][x] != slot and garden[y][x + 1] != slot:
            print(f"Right outer top corner {x=} {y=}")
            corners_count += 1
        if garden[y - 1][x] != slot and garden[y][x - 1] != slot:
            print(f"Left outer top corner {x=} {y=}")
            corners_count += 1
        if garden[y + 1][x] != slot and garden[y][x - 1] != slot:
            print(f"Left outer bottom corner {x=} {y=}")
            corners_count += 1

        if garden[y + 1][x + 1] != slot and garden[y + 1][x] == garden[y][x + 1] == slot:
            print(f"Right inner bottom corner {x=} {y=}")
            corners_count += 1
        if garden[y - 1][x + 1] != slot and garden[y - 1][x] == garden[y][x + 1] == slot:
            print(f"Right inner top corner {x=} {y=}")
            corners_count += 1
        if garden[y - 1][x - 1] != slot and garden[y - 1][x] == garden[y][x - 1] == slot:
            print(f"Left inner top corner {x=} {y=}")
            corners_count += 1
        if garden[y + 1][x - 1] != slot and garden[y + 1][x] == garden[y][x - 1] == slot:
            print(f"Left inner bottom corner {x=} {y=}")
            corners_count += 1

    print()
    return corners_count


def print_matrix(matrix: list[list[chr]]):
    for row in matrix:
        print("".join(row))
    print()


def copy_matrix(matrix: list[list[chr]]) -> list[list[chr]]:
    return [row.copy() for row in matrix]


def process(data: str):
    garden: list[list[chr]] = [list("#" + line + "#") for line in data.splitlines()]
    garden = [["#" for _ in range(len(garden[0]))]] + garden + [["#" for _ in range(len(garden[0]))]]
    original_garden = copy_matrix(garden)
    print_matrix(garden)

    result = 0

    for y in range(len(garden)):
        for x in range(len(garden[y])):
            if garden[y][x] != "#":
                plot = get_plot(garden, garden[y][x], x, y)
                area = get_area(original_garden, plot)
                perimeter = get_perimeter(copy_matrix(original_garden), plot)
                # print(plot)
                print(f"{original_garden[y][x]} {area=} {perimeter=} => {area * perimeter}")
                result += area * perimeter
                # print_matrix(garden)

    print(result)
