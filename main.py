import py5
from countdown import draw_countdown
from block import draw_blocks

# === Status, Input und Time-Block Schritte === #
status = 1 # 1 - Input Status, 2 - Countdown Status
input_step = 0 # Beschreibt was gerade definiert wird (Input-Phase). 0 - Anzahl Dictionary-Entries, 1 - Max (6) - die einzelnen Entries des Dictionaries selbst
time_block_step = 0 # Beschreibt welcher Key im Dictionary Entry gerade definiert wird (Timer-Block-Phase).

# === Zeitvariablen === #
std = 0
m = 0
sk = 0
timerstd = 0
timerm = 0
timersk = 0
last_sk = 0
total_sk = 0

# === Farbe des Countdown & Eingabe === #
redBG = py5.random_int(80,200)
greenBG= py5.random_int(15,55)
blueBG = py5.random_int(80,200)

# === Zeitblöcke & Input - Variablen === #
input_text = ""
num_blocks = 0
temp_blocks = []
blocks = []

def settings():
    w = py5.display_width
    h = py5.display_height
    py5.size(int(w * 0.7), int(h * 0.7))

def setup():
    global std, m, sk, timerstd, timerm, timersk, total_sk

    print("Initialisierung...")
    # === Schriftart für das Programm === #
    py5.text_font(py5.create_font('Raveo-Display-Medium-BF6747d9eb6d8a9.otf', 20))
    print("Schriftart geladen...")
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
        # Erstellt den Titel des Programms, während des Countdowns #
        py5.text_align(py5.RIGHT, py5.BOTTOM)
        py5.fill(0)
        py5.text_size(60)
        py5.text("BlockTimer", py5.width * 0.965, py5.height * 0.15)
        py5.text_align(py5.LEFT, py5.BOTTOM)

        # === Erstellt den Zeitablauf und visuellen Countdown === #
        timersk -= 1/py5.get_frame_rate()
        draw_countdown(total_sk, timerstd, timerm, timersk, redBG, greenBG, blueBG)


def draw_inputscreen():
    global input_step, time_block_step, temp_blocks
    # === Erstellt das Input-Fenster, in dem Nutzer den Timer einstellen können. === #
    py5.fill(0)
    py5.text_size(40)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text("Zeitangaben einstellen - BlockTimer", py5.width / 2, 100)

    # === Gibt einen Text aus, der dem Nutzer beschreibt, was im Moment eingegeben werden soll. === #
    if input_step == 0:
        py5.text_size(32)
        py5.text("Bitte geben Sie hier die Anzahl Zeitblöcke (1 - 6) an.", py5.width / 2, py5.height * 0.8)

    else:
        py5.text_size(32)
        # === Hier sind die Beschreibungen für die einzelnen Time-Block-Phasen in denen Stunden, Minuten, Sekunden
        # === und der Name des TimeBlocks durch den Nutzer definiert werden.
        if time_block_step == 0:
            py5.text(f"Wie viele Stunden sind für den Abschnitt {input_step} geplant?", py5.width / 2, py5.height * 0.8)
        elif time_block_step == 1:
            py5.text(f"Wie viele Minuten sind für den Abschnitt {input_step} geplant?", py5.width / 2, py5.height * 0.8)
        elif time_block_step == 2:
            py5.text(f"Wie viele Sekunden sind für den Abschnitt {input_step} geplant?", py5.width / 2, py5.height * 0.8)
        elif time_block_step == 3:
            py5.text(f"Geben Sie den Namen des Abschnitt {input_step} an", py5.width / 2, py5.height * 0.8)
    # Hier wird die Eingabe des Nutzers wieder ausgegeben, damit der Nutzer sie auch wieder anpassen kann, falls nötig. #
    py5.text_size(90)
    py5.fill(redBG, greenBG, blueBG)
    py5.text(input_text, py5.width / 2, py5.height * 0.5)


def key_pressed():
    global status, input_text, input_step, time_block_step
    # === Definiert in der Input-Phase oder Timer-Block-Phase, wenn welche Tasten ausgelesen werden und teilweise wie viele Zeichen erlaubt sind. === #
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

    # === Verarbeitet das Drücken der Enter-Taste, je nach dem in welche Input-Sequenz oder Timer-Block-Sequenz das Programm befindet. === #

    # Bestimmt, wie viele Zeitblöcke definiert werden können. #
    if input_step == 0:
        if input_text.isdigit() and 1 <= int(input_text) <= 6:
            num_blocks = int(input_text)
            input_text = ""
            input_step = 1
            time_block_step = 0
        else:
            input_text = ""
    # Je nach time_block_step wird andere(r) Key(s) des Dictionaries temp_blocks definiert 0 = Std und Farben, 1 = Min, 2 = Sek, 3 = Name #
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

            # Hier werden die Informationen aus dem Dictionary temp_block in das Dictionary block eingefügt, die totale Zeit wird berechnet
            # und die Variablen std, m, sk, timerstd, timerm und timersk werden festgelegt.
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