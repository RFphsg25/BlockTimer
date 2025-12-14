import py5

def draw_countdown(total_sk,timerstd,timerm,timersk,rval,gval,bval):

    # Berechnet die Umstellung, wenn Sekunden / Minuten auf 0 gehen, #
    # aber noch Stunden / Minuten vorhanden sind. #
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

    # Berechnet die Lönge, die der Countdown-Balken basierend auf der Zeit, die vergangen ist. #
    remain_sk = (timerstd * 60 * 60) + (timerm * 60) + timersk
    progress = 1 - (remain_sk / total_sk)
    total_length = py5.width * 0.93
    current_length = progress * total_length

    # Erstellt die Visualisierung des Countdown-Balkens #
    if current_length < total_length:
        py5.no_stroke()
        py5.fill(rval, gval, bval, 150)
        py5.rect(py5.width * 0.035, py5.height * 0.25, current_length, py5.height * 0.7)

    else:
        py5.fill(rval, gval, bval)
        py5.rect(py5.width * 0.035, py5.height * 0.25, total_length, py5.height * 0.7)

        # Lässt den Text am nach dem Zeitablauf blinken #
        py5.text_size(60)
        if (py5.frame_count // 30) % 2 == 1:
            py5.fill(255)
        else:
            py5.fill(rval, gval, bval)
        py5.text("Die Zeit ist abgelaufen.", py5.width / 3.6, py5.height * 0.62)

