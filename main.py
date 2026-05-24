from utils import *
from random import randint

NAME = "ARES-7"
START_POS = {"x": 0, "y": 0}


def intro() -> None:
    h_line(2)
    print()
    centerText("Deep Space Rover - Mission Kepler 9")
    print()
    h_line(2)
    print()
    centerText("Der Planet Kepler-9b wartet auf dich.")
    centerText("Dein Rover muss eine verlassene Forschungsstation")
    centerText("am anderen Ende des Planeten erreichen.")
    centerText("Die Reise ist sehr Gefährlich.")
    print()
    print("Traust du dich fortzufahren (Ja, Nein)? ", end="")
    while True:
        if input("").lower() in JA:
            break
        print()
        print("Ich habe dich stärker erwartet.")
        print("Überlege dir es nochmal.")
        print("Willst du weitermachen (Ja, Nein)? ", end="")


def parameter() -> None:
    print()
    centerText("[1/7] NAME DES ROVERS", "=")
    for i in range(1, 4):
        NAME = input(
            "Wie soll dein Rover heißen (max. 10 Charaktere)? ").strip()
        if NAME and len(NAME) < 10:
            print()
            print(f"Dein Rover heißt {NAME.upper()}.")
            break
        else:
            if i != 3:
                print()
                print(
                    f"Bitte geben Sie einen gültigen Namen ein. (Noch {3 - i} Versuche)")
            else:
                NAME = "ARES-7"
                print()
                print("Kein gültiger Name")
                print(f"Dein Rover heißt {NAME}")
    print()
    centerText("[2/7] START POSITION", "=")
    print("Wo startet der Rover?")
    for i in range(1, 4):
        try:
            pos_x: int = int(input(
                "Start X (Erlaubt: -100 bis 100): ").strip())
            if pos_x and pos_x in range(-100, 101):
                break
            else:
                raise ValueError
        except ValueError:
            if i != 3:
                print()
                print(
                    f"Bitte geben Sie einen gültigen Namen ein. (Noch {3 - i} Versuche)")
            else:
                pos_x = randint(-70, -30)
                print()
                print("Keine gültige X Position")
                print("Position wird ausgewürfelt")
                print()
    for i in range(1, 4):
        try:
            pos_y: int = int(input(
                "Start Y (Erlaubt: -100 bis 100): ").strip())
            if pos_y and pos_y in range(-100, 101):
                break
            else:
                raise ValueError
        except ValueError:
            if i != 3:
                print()
                print(
                    f"Bitte geben Sie einen gültigen Namen ein. (Noch {3 - i} Versuche)")
            else:
                pos_y = randint(-70, -30)
                print()
                print("Keine gültige Y Position")
                print("Position wird ausgewürfelt")
                print()
    START_POS["x"] = pos_x  # pyright: ignore[reportPossiblyUnboundVariable]
    START_POS["y"] = pos_y  # pyright: ignore[reportPossiblyUnboundVariable]
    print(f"Dein Rover startet bei X:{START_POS['x']} Y:{START_POS['y']}")


def main() -> None:
    # clear()
    # intro()
    clear()
    parameter()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        print("Vielleicht beim nächsten Mal!")
        print("Abbruch...")
        exit()
    except Exception as E:
        print(E)
