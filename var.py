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
        "krater_anzahl": 3,
        "zufall": 15,
        "checkpoints": 2,
        "solarstation": 35,
        "solar_station_anzahl": 4,
        "checkpoint_energie": 50,
        "max_schritt": 100,
    },
    "mittel": {
        "krater": -15,
        "krater_anzahl": 5,
        "zufall": 25,
        "checkpoints": 3,
        "solarstation": 20,
        "solar_station_anzahl": 3,
        "checkpoint_energie": 25,
        "max_schritt": 50,
    },
    "schwer": {
        "krater": -20,
        "krater_anzahl": 7,
        "zufall": 35,
        "checkpoints": 3,
        "solarstation": 10,
        "solar_station_anzahl": 2,
        "checkpoint_energie": 20,
        "max_schritt": 20,
    }
}


SCHRITT_WEITE = 10
RADIUS_KRATER = 10
RADIUS_SOLAR = 8
RADIUS_CHECK = 12
RADIUS_ZIEL = 10

MIN_ABSTAND = 20
