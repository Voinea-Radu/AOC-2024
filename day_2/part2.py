def check_report(report:list[int]):
    ascend: bool = report[0] < report[1]

    for index in range(1, len(report)):
        val_1: int = report[index - 1]
        val_2: int = report[index]
        if val_1 == val_2:
            return False

        if not ascend and val_1 < val_2:
            return False

        if ascend and val_1 >= val_2:
            return False

        if abs(val_1 - val_2) > 3:
            return False

    return True

def process(data: str):
    result: int = 0

    for line in data.splitlines():
        data_line: list[int] = [int(value) for value in line.split(" ")]

        safe_report: bool = False

        for removal_index in range(len(data_line)):
            safe_report = check_report(data_line[:removal_index] + data_line[removal_index + 1:])
            if safe_report:
                break

        if safe_report:
            result += 1

    print(result)
