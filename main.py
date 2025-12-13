import py5
from countdown import countdown


std = 0
m = 1
sk = 5

timerstd = std
timerm = m
timersk = sk
last_sk = 0

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
    countdown(std, m, sk, timerstd, timerm, timersk)

    py5.background(200,200,200)
    py5.text_size(15)
    py5.fill(0, 0, 0)
    py5.text('Hello, this is a functional script.', 50, py5.height / 2)


py5.run_sketch()