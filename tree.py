from copy import deepcopy


class Tree:
    BLOQUE = 0
    ESPACIO_VACIO = 1
    MONEDA = 2
    SIN_ROSTRO = 3
    CHIHIRO = 4
    HAKU = 5

    def __init__(self, *args):
        if len(args) == 1:
            self.movement = "START"
            self.father = None
            self.mapa = list()
            self.x = int()
            self.y = int()
            self.depth = 0
            self.cost = 0
            self.end = False
            self.meta_x = -1
            self.meta_y = -1
            self.load_file(args[0])

        else:
            self.movement = args[0]
            self.father = args[1]
            self.mapa = args[2]
            self.x = args[3]
            self.y = args[4]
            self.depth = args[5]
            self.cost = args[6]
            self.end = args[7]
            self.meta_x = self.father.meta_x
            self.meta_y = self.father.meta_y

        self.children = list()
        self.acumulated_coins = 0
        # print("G(n): " + str(self.g()) + " <= " "H(n): " + str(self.h()))
        # assert self.g() >= self.h()

    def load_children(self):
        if self.end:
            return
        if self.x > 0 and self.mapa[self.y][self.x - 1] != Tree.BLOQUE:
            self.children.append(self.__load_child("LEFT", -1, 0))

        if self.x < len(self.mapa[0]) - 1 and self.mapa[self.y][self.x + 1] != Tree.BLOQUE:
            self.children.append(self.__load_child("RIGHT", 1, 0))

        if self.y > 0 and self.mapa[self.y - 1][self.x] != Tree.BLOQUE:
            self.children.append(self.__load_child("UP", 0, -1))

        if self.y < len(self.mapa) - 1 and self.mapa[self.y + 1][self.x] != Tree.BLOQUE:
            self.children.append(self.__load_child("DOWN", 0, 1))

    def __load_child(self, movement, dx, dy):

        x = self.x + dx
        y = self.y + dy
        cost = 0
        end = False
        if self.mapa[y][x] == Tree.ESPACIO_VACIO:
            cost += 1
        elif self.mapa[y][x] == Tree.MONEDA:
            cost += 2
            self.acumulated_coins += 1
        elif self.mapa[y][x] == Tree.SIN_ROSTRO:
            cost += 2
            cost -= 5 * self.acumulated_coins
            self.acumulated_coins = 0
        elif self.mapa[y][x] == Tree.HAKU:
            cost += 1
            end = True
        mapa = deepcopy(self.mapa)
        mapa[self.y][self.x] = Tree.ESPACIO_VACIO
        mapa[y][x] = Tree.CHIHIRO
        depth = self.depth + 1
        cost += self.cost
        return Tree(movement, self, mapa, x, y, depth, cost, end)

    def g(self):
        # return abs(self.x - self.meta_x) + abs(self.y - self.meta_y)
        return self.cost

    def h(self):
        # return math.sqrt(math.pow(self.x - self.meta_x, 2) + math.pow(self.y - self.meta_y, 2))
        return abs(self.x - self.meta_x) + abs(self.y - self.meta_y)

    def f(self):
        return self.g() + self.h()

    def __str__(self):
        string = self.movement + "\n"
        string += "POSITION: " + str(self.x) + " " + str(self.y) + " " + str(self.mapa[self.y][self.x]) + "\n"
        string += "COST: " + str(self.cost) + "\n"
        string += "DEPTH: " + str(self.depth) + "\n"
        string += "RUTE:" + self.calculate_rute() + "\n"
        string += "\t\t\tBOARD\n"

        for sup in self.mapa:
            string += str(sup) + "\n"
        return string

    def calculate_rute(self):
        node = self
        rute = ""
        while node is not None:
            rute = " -> " + node.movement + rute
            node = node.father
        return rute

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
                        self.x = width
                        self.y = heigth
                    elif char == '5':
                        self.meta_x = width
                        self.meta_y = heigth
                    temporal_line.append(int(char))
                width += 1
            mapa.append(temporal_line)
            heigth += 1
        self.mapa = mapa
