import py5
from countdown import draw_countdown
from block import draw_blocks

# === Zeitvariablen === #
std = 0
m = 0
sk = 0
timerstd = 0
timerm = 0
timersk = 0
last_sk = 0
total_sk = 0

# === Farben für Zeitblöcke === #
red1 = py5.random_int(100,200)
green1 = py5.random_int(100,200)
blue1 = py5.random_int(100,200)
red2 = py5.random_int(100,200)
green2 = py5.random_int(100,200)
blue2 = py5.random_int(100,200)
red3 = py5.random_int(100,200)
green3 = py5.random_int(100,200)
blue3 = py5.random_int(100,200)

# === Farbe des Countdown === #
redBG = py5.random_int(180,200)
greenBG= py5.random_int(15,35)
blueBG = py5.random_int(5,25)

# === Zeitblöcke - Variablen === #
blocks = [
    {"name": "Einführung", "std": 0, "m": 0, "sk": 5, "r": red1, "g": green1, "b": blue1},
    {"name": "Gruppenphase", "std": 0, "m": 0, "sk": 5, "r": red2, "g": green2, "b": blue2},
    {"name": "Abschluss", "std": 0, "m": 0, "sk": 5, "r": red3, "g": green3, "b": blue3},
]


def settings():

    # === Block- und Zeitvariablen === #

    w = py5.display_width
    h = py5.display_height
    py5.size(int(w * 0.7), int(h * 0.7))

def setup():
    global std, m, sk, timerstd, timerm, timersk, total_sk

    print("Initialisierung...")
    print("Bildwiederholrate: " + str(py5.get_frame_rate()) + "fps")

    # === Berechnen der Gesamtzeit aus Block-Liste === #
    for block in blocks:
        total_sk += (block["std"] * 3600) + (block["m"] * 60) + block["sk"]

    # Gesamtzeit in Sekunden auf Stunden, Minuten und Sekunden verteilen #
    std = total_sk // 3600
    m = (total_sk % 3600) // 60
    sk = total_sk % 60

    print("Gesamtzeit: " + str(std) + ":" + str(m) + ":" + str(sk))

    # === Countdown-Zeit festlegen und initialisieren === #
    timerstd = std
    timerm = m
    timersk = sk

def draw():
    global std, m, sk, timersk, timerm, timerstd, last_sk, total_sk

    py5.background(235, 235, 235)
    # === Erstellt die Zeitblöcke === #
    draw_blocks(blocks, total_sk)

    # === Erstellt den Zeitablauf und visuellen Countdown === #
    timersk -= 1/py5.get_frame_rate()
    draw_countdown(total_sk, timerstd, timerm, timersk, redBG, greenBG, blueBG)

py5.run_sketch()