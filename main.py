import py5

from countdown import countdown

# === Zeitvariablen === #
std = 0
m = 1
sk = 5
timerstd = std
timerm = m
timersk = sk
last_sk = 0

# === Farben für Zeitblöcke === #
# == Farbe 1 == #
red1 = py5.random_int(0,255)
green1 = py5.random_int(0,255)
blue1 = py5.random_int(0,255)
# == Farbe 2 == #
red2 = py5.random_int(0,255)
green2 = py5.random_int(0,255)
blue2 = py5.random_int(0,255)
# == Farbe 3 == #
red3 = py5.random_int(0,255)
green3 = py5.random_int(0,255)
blue3 = py5.random_int(0,255)

# === Farbe des Countdown === #
redH = py5.random_int(0,25)
greenH = py5.random_int(0,25)
blueH = py5.random_int(0,25)



def settings():

    w = py5.display_width
    h = py5.display_height
    py5.size(int(w * 0.7), int(h * 0.7))

def setup():

    print("Initializing...")
    print(py5.get_frame_rate())

def draw():
    global std, m, sk, timersk, timerm, timerstd, last_sk



    # ==== Erstellt den Zeitablauf ==== #
    timersk -= 1/py5.get_frame_rate()
    countdown(std, m, sk, timerstd, timerm, timersk, redH, greenH, blueH)

py5.run_sketch()