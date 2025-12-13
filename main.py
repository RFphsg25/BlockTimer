import py5
from countdown import countdown

# ==== Input Variablen ==== #
std = 0
m = 0
sk = 30
timerstd = 0
timerm = 0
timersk = 0

def settings():
    py5.size(int(py5.display_width * 0.7), int(py5.display_height * 0.7))

def setup():
    global timerstd, timerm, timersk

    timerstd = std
    timerm = m
    timersk = sk

    print("Initializing...")
    print(py5.get_frame_rate())

def draw():
    global std, m, sk, timerstd, timerm, timersk

    py5.background(200, 200, 200)
    py5.text_size(15)
    py5.fill(0, 0, 0)
    py5.text('Hello.', 50, py5.height / 2)

    timersk -= 1/py5.get_frame_rate()
    countdown(std, m, sk, timerstd, timerm, timersk)

py5.run_sketch()