def process(data: str):
    result: int = 0

    for line in data.splitlines():
        data_line: list[int] = [int(value) for value in line.split(" ")]

        ascend: bool = True

        if (data_line[0] > data_line[1]):
            ascend = False

        checks_requirements: bool = True

        for index in range(1, len(data_line)):
            val_1: int = data_line[index]
            val_2: int = data_line[index - 1]

            if ascend and val_1 < val_2:
                checks_requirements = False
                break
            if not ascend and val_1 > val_2:
                checks_requirements = False
                break

            if val_1 == val_2:
                checks_requirements = False
                break

            if abs(val_1 - val_2) > 3:
                checks_requirements = False
                break

        if checks_requirements:
            result += 1

    print(result)
