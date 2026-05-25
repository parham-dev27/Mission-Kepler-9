from os import system, name
from shutil import get_terminal_size


def clear() -> None:
    system("cls" if name == "nt" else "clear")


def h_line(line_num: int = 1) -> None:
    for _ in range(line_num):
        print("=" * get_terminal_size().columns)


def centerText(text, filler=" ") -> None:
    print(f"{text}".center(get_terminal_size().columns, filler))
