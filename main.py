def cargar(ruta: str):
    file = open(ruta)
    content = file.readlines()

    board = str()
    width = int()
    height = 0
    for line in content:
        if line[0] == '#':
            continue

        board += line
        width = int(max(len(line) / 2, width))
        height += 1

    print("EL tamaño del mapa es: {}x{}".format(width, height))

    board = board.replace(",", "")
    board += "\n"

    mapa = list()
    temporal_line = list()
    for char in board:
        if char == '\n':
            mapa.append(temporal_line)
            temporal_line = list()
        else:
            temporal_line.append(int(char))


cargar("map/map1.txt")
