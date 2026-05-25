from utils import *
from var import *
from random import randint

NAME: str = "ARES-7"
PLAYER = {"x": 0, "y": 0}
START_WINKEL: int = 0
SCHWIERIGKEITSGRAD: str = "mittel"

WORLD = {
    "krater": [],
    "solarstation": [],
    "checkpoint": [],
    "ziel": []
}


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
    """
        NAME
    """
    global NAME
    print()
    centerText("[1/4] NAME DES ROVERS", "=")
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
    """
        START POSITION
    """
    global PLAYER
    print()
    centerText("[2/4] START POSITION", "=")
    print("Wo startet der Rover?")
    for i in range(1, 4):
        try:
            pos_x: int = int(input(
                "Start X (Erlaubt: -100 bis 100): ").strip())
            if str(pos_x) and pos_x in range(-100, 101):
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
            if str(pos_y) and pos_y in range(-100, 101):
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
                print("Position wird ausgewürfelt.")
    PLAYER["x"] = pos_x  # pyright: ignore[reportPossiblyUnboundVariable]
    PLAYER["y"] = pos_y  # pyright: ignore[reportPossiblyUnboundVariable]
    print()
    print(f"Dein Rover startet bei X:{PLAYER['x']} Y:{PLAYER['y']}")
    """
        START WINKEL
    """
    global START_WINKEL
    print()
    centerText("[3/4] START WINKEL", "=")
    print("In welche Richtung schaut der Rover beim START?")
    print("0°=Ost, 90°=Nord, 180°=West, 270°=Süd")
    for i in range(1, 4):
        winkel = input(
            "Startwinkel (0–359) oder Richtung (N/S/O/W): ").strip().upper()
        if str(winkel) and winkel in RICHTUNGEN:
            START_WINKEL = RICHTUNGEN[winkel]
            break
        try:
            winkel = int(winkel)
            if winkel in range(0, 330):
                START_WINKEL = winkel
                break
            raise ValueError
        except ValueError:
            if i != 3:
                print()
                print(
                    f"Bitte geben Sie einen gültigen Winkel ein. (Noch {3 - i} Versuche)")
            else:
                START_WINKEL = randint(0, 359)
                print()
                print("Ungültiger Winkel")
                print("Winkel wird ausgewürfelt.")
    print()
    print(f"Dein Startwinkel beträgt {START_WINKEL}°")  # type: ignore
    """
        SCHWIERIGKEITSGRAD
    """
    global SCHWIERIGKEITSGRAD
    print()
    centerText("[4/4] SCHWIERIGKEITSGRAD", "=")
    print("Wie schwer willst du es haben?")
    print("1 = Leicht")
    print("    • Zufallsereignisse treten selten auf (15% pro Schritt)")
    print("    • Krater verursachen wenig Schaden (-10 Energie)")
    print("    • 2 Checkpoints")
    print("    • Empfohlen für den ersten Versuch")
    print()
    print("2 = Mittel")
    print("    • Zufallsereignisse treten regelmäßig auf (25% pro Schritt)")
    print("    • Krater verursachen normalen Schaden (-15 Energie)")
    print("    • 3 Checkpoints")
    print("    • Ausgeglichene Herausforderung")
    print()
    print("3 = Schwer")
    print("    • Zufallsereignisse treten häufig auf (35% pro Schritt)")
    print("    • Krater verursachen starken Schaden (-20 Energie)")
    print("    • 3 Checkpoints")
    print("    • Nur für erfahrene Rover-Piloten")

    for i in range(1, 4):
        try:
            grad = int(input("Schwierigkeit (1/2/3): ").strip())
            if str(grad) and grad in range(1, 4):
                SCHWIERIGKEITSGRAD = list(SCHWIERIGKEITSGRAD_KRITERIEN.keys())[
                    grad - 1]
                break
            raise ValueError
        except ValueError:
            if i != 3:
                print()
                print(
                    f"Bitte geben Sie einen gültigen Wert ein. (Noch {3 - i} Versuche)")
            else:
                SCHWIERIGKEITSGRAD = list(
                    SCHWIERIGKEITSGRAD_KRITERIEN.keys())[1]
                print()
                print("Üngültig")
    print()
    print(f"Schwierigkeitsgrad: {SCHWIERIGKEITSGRAD}")  # type: ignore


def zusammenfassung():
    h_line()
    centerText("Zusammenfassung")
    h_line()
    centerText(f"Rover-Name: {NAME.upper()}")
    centerText(f"Startposition: ({PLAYER['x']}|{PLAYER['y']})")
    centerText(f"Startwinkel: {START_WINKEL}°")
    centerText(
        f"Schwierigkeit: {SCHWIERIGKEITSGRAD.capitalize()}")
    h_line()
    print("Fortfahren (Ja/Nein)? ", end="")
    if input("").lower() in JA:
        return
    else:
        raise ConnectionRefusedError


def generateWorld():
    global WORLD
    match getQuad(PLAYER):
        case 5:
            WORLD["ziel"].append(getValidCords(WORLD))
        case 4:
            WORLD["ziel"].append(getValidCords(WORLD, 2))
        case 3:
            WORLD["ziel"].append(getValidCords(WORLD, 1))
        case 2:
            WORLD["ziel"].append(getValidCords(WORLD, 4))
        case 1:
            WORLD["ziel"].append(getValidCords(WORLD, 3))

            # ZIEL FERTIG WEITER MORGEN


def main() -> None:
    # clear()
    # intro()
    # while True:
    #     try:
    #         clear()
    #         parameter()
    #         clear()
    #         zusammenfassung()
    #         break
    #     except ConnectionRefusedError:
    #         continue
    generateWorld()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        print("Vielleicht beim nächsten Mal!")
        print("Abbruch...")
        exit()
    except Exception as E:
        raise Exception
