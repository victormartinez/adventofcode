from pathlib import Path


def get_file_rows():
    return filter(lambda x: bool(x), Path("input.txt").read_text().split("\n"))


def find_numbers(sorted_numbers):
    for first_number in sorted_numbers:
        for second_number in reversed(sorted_numbers):
            plus = first_number + second_number
            if plus == 2020:
                return first_number, second_number

            if plus < 2020:
                break

    return None, None


def execute():
    all_numbers = list(map(lambda x: int(x), get_file_rows()))
    first, second = find_numbers(sorted(all_numbers))

    print(f"Numbers: {first} & {second}")
    print(f"Challenge result: {first * second}")


if __name__ == "__main__":
    execute()
