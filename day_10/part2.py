DIRECTIONS: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find_trails(map: list[list[int]], x: int, y: int, target_height: int) -> int:
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        return 0

    if map[y][x] != target_height:
        return 0

    if map[y][x] == 9:
        output = set()
        output.add((y, x))
        return 1

    result = 0

    for direction in DIRECTIONS:
        result += find_trails(map, x + direction[0], y + direction[1], target_height + 1)

    return result


def process(data: str):
    map: list[list[int]] = [[int(char) for char in line] for line in data.splitlines()]
    result = 0

    for y in range(len(map)):
        for x in range(len(map[0])):
            local_result = find_trails(map, x, y, 0)
            result += local_result
            if local_result > 0:
                print(f"({y}, {x}) -> {local_result}")

    print(result)
