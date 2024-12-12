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


def get_perimeter(garden: list[list[chr]], plot: list[tuple[int, int]]) -> int:
    if len(plot) == 0:
        return 0

    perimeter = 4 * len(plot)

    for x, y in plot:
        for dx, dy in DIRECTIONS:
            if garden[y + dy][x + dx] == garden[y][x]:
                perimeter -= 1

    return perimeter


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
                perimeter = get_perimeter(original_garden, plot)
                # print(plot)
                print(f"{original_garden[y][x]} {area=} {perimeter=} => {area * perimeter}")
                result+= area * perimeter
                # print_matrix(garden)

    print(result)