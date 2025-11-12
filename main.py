import py5

std = 0
m = 0
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

    timersk -= 1/py5.get_frame_rate()

    if timersk < 0:
        if timerstd > 0 or timerm > 0:
            timersk = 60 + timersk
            timerm -= 1
        else:
            timersk = 0

    if timerm < 0:
        if timerstd > 0:
            timerm = 59
            timerstd -= 1
        else:
            timerm = 0
    if timerstd < 0:
        timerstd = 0
        timerm = 0
        timersk = 0

    total_sk = (std * 60 * 60) + (m * 60) + sk
    remain_sk = (timerstd * 60 * 60) + (timerm * 60) + timersk
    progress = 1 - (remain_sk / total_sk)
    a = progress * py5.width
    py5.background(200,200,200)
    py5.text_size(15)
    py5.fill(0, 0, 0)
    py5.text('Hello, this is a functional script.', 50, py5.height / 2)
    if a < py5.width:
        py5.no_stroke()
        py5.fill(200, 90, 100, 80)
        py5.rect(0,py5.height-(py5.height*0.6), a, py5.height*0.6)
        py5.fill(0,0,0)
        py5.text(str(int(timerstd)) + " :Stunden " + str(int(timerm)) + ' :Minuten ' + str(int(timersk)) + ' :Sekunden', 50, py5.height / 3)
    else:
        py5.fill(200, 90, 100, 80)
        py5.rect(0,py5.height-(py5.height*0.6),py5.width, py5.height*0.6)


py5.run_sketch()