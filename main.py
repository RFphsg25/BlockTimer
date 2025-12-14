import py5
from countdown import draw_countdown
from block import draw_blocks

# === Status und Input-Variablen === #
status = 1

input_text = ""
input_step = 0
time_block_step = 0
temp_blocks = []
num_blocks = 0

# === Zeitvariablen === #
std = 0
m = 0
sk = 0
timerstd = 0
timerm = 0
timersk = 0
last_sk = 0
total_sk = 0

# === Farbe des Countdown === #
redBG = py5.random_int(180,200)
greenBG= py5.random_int(15,35)
blueBG = py5.random_int(5,25)

# === Zeitblöcke - Variablen === #
blocks = []


def settings():

    # === Block- und Zeitvariablen === #

    w = py5.display_width
    h = py5.display_height
    py5.size(int(w * 0.7), int(h * 0.7))

def setup():
    global std, m, sk, timerstd, timerm, timersk, total_sk

    print("Initialisierung...")
    print("Bildwiederholrate: " + str(py5.get_frame_rate()) + "fps")

def draw():
    global std, m, sk, timersk, timerm, timerstd, last_sk, total_sk

    py5.background(235, 235, 235)
    if status == 1:
        # === Erstellt den Eingabebildschirm für die Inhaltsangabe === #
        draw_inputscreen()

    elif status == 2:
        # === Erstellt die Zeitblöcke === #
        draw_blocks(blocks, total_sk)

        # === Erstellt den Zeitablauf und visuellen Countdown === #
        timersk -= 1/py5.get_frame_rate()
        draw_countdown(total_sk, timerstd, timerm, timersk, redBG, greenBG, blueBG)


def draw_inputscreen():
    global input_step, time_block_step, num_blocks, temp_blocks

    py5.fill(0)
    py5.text_size(40)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text("Zeitangaben einstellen - BlockTimer", py5.width / 2, 100)

    if input_step == 0:
        py5.text_size(32)
        py5.text("Bitte geben Sie hier die Anzahl Zeitblöcke (1 - 6) an.", py5.width / 2, py5.height * 0.8)

    else:
        py5.text_size(32)

        if time_block_step == 0:
            py5.text(f"Wie viele Stunden sind für den Abschnitt {input_step} geplant?", py5.width / 2, py5.height * 0.8)
        elif time_block_step == 1:
            py5.text(f"Wie viele Minuten sind für den Abschnitt {input_step} geplant?", py5.width / 2, py5.height * 0.8)
        elif time_block_step == 2:
            py5.text(f"Wie viele Sekunden sind für den Abschnitt {input_step} geplant?", py5.width / 2, py5.height * 0.8)
        elif time_block_step == 3:
            py5.text(f"Geben Sie den Namen des Abschnitt {input_step} an", py5.width / 2, py5.height * 0.8)

    py5.text_size(48)
    py5.fill(0, 100, 200)
    py5.text(input_text + "_", py5.width / 2, py5.height * 0.6)


def key_pressed():
    global status, input_text, input_step, time_block_step

    if status == 1:
        if py5.key_code == 10:
            handle_enter()

        elif py5.key_code == 8:
            input_text = input_text[:-1]

        else:

            if input_step  == 0 or time_block_step in [0, 1, 2]:
                if py5.key.isdigit() and py5.key_code not in [10, 8, 16]:
                    input_text += py5.key

            elif time_block_step == 3:
                if len(input_text) < 20 and py5.key_code not in [10, 8, 16]:
                    input_text += py5.key



def handle_enter():
    global status, input_step, time_block_step, input_text, temp_blocks, num_blocks
    global blocks, std, m, sk, timerstd, timerm, timersk, total_sk

    if input_step == 0:
        if input_text.isdigit() and 1 <= int(input_text) < 7:
            num_blocks = int(input_text)
            input_text = ""
            input_step = 1
            time_block_step = 0
        else:
            input_text = ""

    elif time_block_step == 0:
        if input_text.isdigit():
            temp_blocks.append({
                "name": "",
                "std": int(input_text),
                "m": 0,
                "sk": 0,
                "r": py5.random_int(100, 200),
                "g": py5.random_int(100, 200),
                "b": py5.random_int(100, 200),
            })
            input_text = ""
            time_block_step = 1
        else:
            input_text = ""

    elif time_block_step == 1:
        if input_text.isdigit():
            temp_blocks[-1]["m"] = int(input_text)
            input_text = ""
            time_block_step = 2
        else:
            input_text = ""

    elif time_block_step == 2:
        if input_text.isdigit():
            temp_blocks[-1]["sk"] = int(input_text)
            input_text = ""
            time_block_step = 3
        else:
            input_text = ""

    elif time_block_step == 3:
        if len(input_text) > 0:
            temp_blocks[-1]["name"] = input_text
            input_text = ""

            if len(temp_blocks) >= num_blocks:
                blocks = temp_blocks.copy()

                total_sk = 0
                for block in blocks:
                    total_sk += (block["std"] * 3600) + (block["m"] * 60) + block["sk"]

                std = total_sk // 3600
                m = (total_sk % 3600) // 60
                sk = total_sk % 60

                timerstd = std
                timerm = m
                timersk = sk

                status = 2
                print(f"Gesamtzeit: {std}:{m}:{sk}")
            else:
                time_block_step = 0
                input_step += 1
        else:
            input_text = ""

py5.run_sketch()