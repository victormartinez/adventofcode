from pathlib import Path


def get_file_rows():
    return filter(lambda x: bool(x), Path("input.txt").read_text().split("\n"))


def parse_row(row):
    row = row.replace(":", "")
    row = row.replace("-", " ")
    min_, max_, char, password = row.split(" ")
    return int(min_), int(max_), char, password


def count_valid_passwords(rows):
    valids = []
    for r in rows:
        min_, max_, char, password = parse_row(r)
        number = password.count(char)
        valids.append(min_ <= number <= max_)
    return sum(valids)


def execute():
    rows = get_file_rows()
    result = count_valid_passwords(rows)
    print(f"Valid passwords: {result}")


if __name__ == "__main__":
    execute()
