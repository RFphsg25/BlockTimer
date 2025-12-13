import py5
from tkinter import *

window = Tk()
window.title("Zeiteneingabe")
window.mainloop()
from countdown import countdown

# === Zeitvariablen === #
std = 0
m = 0
sk = 30
timerstd = 0
timerm = 0
timersk = 0
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
grayH = py5.random_int(0,25)


def settings():
    w = py5.display_width
    h = py5.display_height
    py5.size(int(w * 0.7), int(h * 0.7))

def setup():
    global std, m, sk, timerstd, timerm, timersk

    print("Initializing...")
    print(py5.get_frame_rate())

    # === tkinter Inputfenster === #


    timerstd = std
    timerm = m
    timersk = sk

def draw():
    global std, m, sk, timersk, timerm, timerstd, last_sk

    py5.background(235, 235, 235)

    # ==== Erstellt den Zeitablauf ==== #
    timersk -= 1/py5.get_frame_rate()
    countdown(std, m, sk, timerstd, timerm, timersk, grayH, grayH, grayH)

py5.run_sketch()