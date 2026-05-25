from os import system, name
from shutil import get_terminal_size
from math import sqrt
from random import randint


def clear() -> None:
    system("cls" if name == "nt" else "clear")


def h_line(line_num: int = 1) -> None:
    for _ in range(line_num):
        print("=" * get_terminal_size().columns)


def centerText(text, filler=" ") -> None:
    print(f"{text}".center(get_terminal_size().columns, filler))


def abstand(cord1: dict, cord2: dict) -> int:
    return round(sqrt(((cord2["x"] - cord1["x"])**2) + ((cord2["y"] - cord1["y"])**2)))


def positionGueltig(player: dict, cords: dict) -> bool:
    for i in list(cords.keys()):
        for j in cords[i]:
            if abstand(player, j) < 20:
                return False
    return True


def genCords(quad: int = 0) -> dict:
    if quad == 1:
        return {"x": randint(-90, 5), "y": randint(5, 90)}
    elif quad == 2:
        return {"x": randint(5, 90), "y": randint(5, 90)}
    elif quad == 3:
        return {"x": randint(5, 90), "y": randint(-90, -5)}
    elif quad == 4:
        return {"x": randint(-90, -5), "y": randint(-90, -5)}

    return {"x": randint(-90, 90), "y": randint(-90, 90)}


def getValidCords(cords: dict, quad: int = 0, ) -> dict:
    while True:
        cord = genCords(quad)
        if positionGueltig(cord, cords):
            return cord


def getQuad(cord: dict) -> int:
    if cord["x"] > 0 and cord["y"] > 0:
        return 2
    elif cord["x"] < 0 and cord["y"] > 0:
        return 1
    elif cord["x"] > 0 and cord["y"] < 0:
        return 3
    elif cord["x"] < 0 and cord["y"] < 0:
        return 4
    return 5
