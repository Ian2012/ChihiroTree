class Tree:

    def __init__(self, ruta):
        self.__mapa = list()
        self.__x = int()
        self.__y = int()

        self.load_file(ruta)
        self.children = list()
        print(self.__x, self.__y)
        print(self.__mapa[self.__y][self.__x])
        for line in self.__mapa:
            print(line)
        # self.load_children()

    def load_file(self, ruta: str):
        file = open(ruta)
        content = file.readlines()

        board = str()
        mapa = list()
        heigth = 0
        for line in content:
            if line[0] == '#':
                continue

            board += line
            line = line.replace(",", "")
            temporal_line = list()
            width = 0

            for char in line:
                if char != "\n":
                    if char == '4':
                        self.__x = width
                        self.__y = heigth
                    temporal_line.append(int(char))
                width += 1
            mapa.append(temporal_line)
            heigth += 1
        self.__mapa = mapa

    def load_children(self):
        pass


tree = Tree("map/map1.txt")
