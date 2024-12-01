def read_inputs() -> tuple[str, str]:
    with open("input/sample") as file:
        sample_data: str = file.read()

    with open("input/real") as file:
        real_data: str = file.read()

    return sample_data, real_data
