import py5

def countdown(std,m,sk,timerstd,timerm,timersk):

rdcol1 = 0
rdcol2 = 0
rdcol3 = 0

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
    if a < py5.width:
        py5.no_stroke()
        py5.fill(200, 90, 100, 80)
        py5.rect(0, py5.height - (py5.height * 0.6), a, py5.height * 0.6)
        py5.fill(0, 0, 0)
        py5.text(str(int(timerstd)) + " :Stunden " + str(int(timerm)) + ' :Minuten ' + str(int(timersk)) + ' :Sekunden',
                 50, py5.height / 3)
    else:
        py5.fill(200, 90, 100, 80)
        py5.rect(0, py5.height - (py5.height * 0.6), py5.width, py5.height * 0.6)

