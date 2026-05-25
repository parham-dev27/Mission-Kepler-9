from os import system, name
from shutil import get_terminal_size


def clear() -> None:
    system("cls" if name == "nt" else "clear")


def h_line(line_num: int = 1) -> None:
    for _ in range(line_num):
        print("=" * get_terminal_size().columns)


def centerText(text, filler=" ") -> None:
    print(f"{text}".center(get_terminal_size().columns, filler))


JA = {"ja", "j", "jawohl", "jo", "jap", "jup", "klar", "okay", "ok", "oki", "okey", "einverstanden", "passt",
      "stimmt", "genau", "yes", "y", "yeah", "yep", "yup", "sure", "alright", "affirmative", "true", "t"}

RICHTUNGEN = {
    "N": 90,
    "NO": 45,
    "O": 0,
    "SO": 315,
    "S": 270,
    "SW": 225,
    "W": 180,
    "NW": 135
}

SCHWIERIGKEITSGRAD_KRITERIEN = {
    "leicht": {
        "krater": -10,
        "zufall": 15,
        "checkpoints": 2,
        "solarstation": 35,
        "checkpoint_energie": 50,
        "max_schritt": 100,
    },
    "mittel": {
        "krater": -15,
        "zufall": 25,
        "checkpoints": 3,
        "solarstation": 20,
        "checkpoint_energie": 25,
        "max_schritt": 50,
    },
    "schwer": {
        "krater": -20,
        "zufall": 35,
        "checkpoints": 3,
        "solarstation": 10,
        "checkpoint_energie": 20,
        "max_schritt": 20,
    }
}
