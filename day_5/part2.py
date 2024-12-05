def check_print(dependencies_map: dict[int, list[int]], pages: list[int]) -> bool:
    for pageIndex in range(len(pages)-1, -1, -1):
        page = pages[pageIndex]

        if page not in dependencies_map:
            continue

        dependencies = dependencies_map[page]

        for followingPageIndex in range(pageIndex+1, len(pages)):
            followingPage = pages[followingPageIndex]

            if followingPage in dependencies:
                tmp = pages[pageIndex]
                pages[pageIndex] = pages[followingPageIndex]
                pages[followingPageIndex] = tmp
                return False

    return True


def process(data: str):
    result = 0
    dependencies_list_str, prints_str = data.split("\n\n")
    dependencies_list = [(int(line.split("|")[0]), int(line.split("|")[1])) for line in dependencies_list_str.splitlines()]
    prints = [[int(page) for page in line.split(",")] for line in prints_str.splitlines()]

    dependencies_map: dict[int, list[int]] = {}

    for dependency, dependent in dependencies_list:
        if dependent not in dependencies_map:
            dependencies_map[dependent] = []
        dependencies_map[dependent].append(dependency)

    for pages in prints:
        pages_copy = pages[::]

        while not check_print(dependencies_map, pages):
            pass

        if pages != pages_copy:
            result += pages[len(pages) // 2]

    print(result)
