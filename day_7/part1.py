def compute(numbers: list[int], operators: list[int]) -> int:
    result: int = numbers[0]

    for index in range(1, len(numbers)):
        if operators[index - 1] == 0:
            result += numbers[index]
        elif operators[index - 1] == 1:
            result *= numbers[index]

    return result


def number_to_base(n: int, base: int) -> list[int]:
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return digits[::-1]


def print_equation(numbers: list[int], operators: list[int], result: int):
    for index in range(len(numbers)):
        print(numbers[index], end=" ")
        if index < len(operators):
            if operators[index] == 0:
                print("+", end=" ")
            else:
                print("*", end=" ")
    print(f"= {result}")


def process(data: str):
    output: int = 0

    lines: list[str] = data.splitlines()

    for line in lines:
        result: int = int(line.split(":")[0])
        numbers: list[int] = []

        for number in line.split(":")[1].strip().split(" "):
            numbers.append(int(number))

        for tmp in range(2 ** (len(numbers) - 1)):
            operators: list[int] = number_to_base(tmp, 2)
            operators = [0] * (len(numbers) - len(operators) - 1) + operators
            if compute(numbers, operators) == result:
                output += result
                print_equation(numbers, operators, result)
                break

    print(output)
