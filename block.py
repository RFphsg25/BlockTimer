import py5

def draw_blocks(blocks,time):
    # === Zeichnet die Blöcke im Hintergrund, die die Zeitabschnitte darstellen.  === #

    # Startpunkt #
    x_pos = 0
    block_height = py5.height * 0.7
    y_pos = (py5.height * 0.95) - block_height

    for block in blocks:

        # Gesamtzeit pro Block in Sekunden #
        block_sk = (block["std"] * 3600) + (block["m"] * 60) + block["sk"]

        # Prozentuale Breite des Blockes basierend der Gesamtzeit #
        block_width = (block_sk/time) * (py5.width * 0.93)

        # Zeichnen der Blöcke #
        py5.no_stroke()
        py5.fill(block["r"], block["g"], block["b"])
        py5.rect(x_pos + py5.width * 0.035, y_pos, block_width, block_height)

        # Benennung der Blöcke #
        py5.fill(block["r"], block["g"], block["b"])
        py5.text_size(20)
        py5.text_align(py5.LEFT, py5.BOTTOM)
        py5.text(block["name"],x_pos + py5.width * 0.035, y_pos - 10)

        # nächster Startpunkt für x-Koordinate = Darstellung der Blöcke nebeneinander #
        x_pos += block_width
