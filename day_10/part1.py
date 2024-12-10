DIRECTIONS: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find_trails(map: list[list[int]], x: int, y: int, target_height: int) -> set[tuple[int, int]]:
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        return set()

    if map[y][x] != target_height:
        return set()

    if map[y][x] == 9:
        output = set()
        output.add((y, x))
        return output

    result = set()

    for direction in DIRECTIONS:
        local_result = find_trails(map, x + direction[0], y + direction[1], target_height + 1)
        result = result.union(local_result)

    return result


def process(data: str):
    map: list[list[int]] = [[int(char) for char in line] for line in data.splitlines()]
    result = 0

    for y in range(len(map)):
        for x in range(len(map[0])):
            local_result = find_trails(map, x, y, 0)
            result+= len(local_result)
            if len(local_result) > 0:
                print(f"({y}, {x}) -> {len(local_result)}")

    print(result)