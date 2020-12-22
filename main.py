def cargar(ruta: str):
    file = open(ruta)
    content = file.readlines()

    board = str()
    mapa = list()
    for line in content:
        if line[0] == '#':
            continue

        board += line
        line = line.replace(",", "")
        temporal_line = list()
        for char in line:
            if char != "\n":
                temporal_line.append(int(char))
        mapa.append(temporal_line)

    return mapa


print(cargar("map/map1.txt"))
