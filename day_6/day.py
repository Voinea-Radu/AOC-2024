from utils.utils import read_inputs
import argparse
from part1 import process as part1
from part2 import process as part2


def main():
    sample_data, real_data = read_inputs()

    parser = argparse.ArgumentParser()
    parser.add_argument("--sample", help="Run the sample data", action="store_true")
    parser.add_argument("--real", help="Run the real data", action="store_true")
    parser.add_argument("--part1", help="Run part 1", action="store_true")
    parser.add_argument("--part2", help="Run part 2", action="store_true")
    args = parser.parse_args()

    if args.sample:
        if args.part1:
            part1(sample_data)
        if args.part2:
            part2(sample_data)

    if args.real:
        if args.part1:
            part1(real_data)
        if args.part2:
            part2(real_data)


if __name__ == '__main__':
    main()
