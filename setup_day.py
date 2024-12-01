import argparse
import shutil


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("day", help="Run the sample data", type=int)
    args = parser.parse_args()

    shutil.copytree(".template", f"day_{args.day}")

if __name__ == '__main__':
    main()
