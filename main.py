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

            self.load_file(args[0])

        else:
            self.movement = args[0]
            self.father = args[1]
            self.mapa = args[2]
            self.x = args[3]
            self.y = args[4]
            self.depth = args[5]
            self.cost = args[6]

        self.children = list()
        self.find_coin = False
        self.end = False

    def load_children(self):
        if self.end:
            return
        if self.x > 0 and self.mapa[self.x - 1][self.y] != Tree.BLOQUE:
            self.children.append(self.__load_child("LEFT", -1, 0))

        if self.x < len(self.mapa[0]) - 1 and self.mapa[self.x + 1][self.y] != Tree.BLOQUE:
            self.children.append(self.__load_child("RIGHT", 1, 0))

        if self.y > 0 and self.mapa[self.x][self.y - 1] != Tree.BLOQUE:
            self.children.append(self.__load_child("UP", 0, -1))

        if self.y < len(self.mapa) - 1 and self.mapa[self.x][self.y + 1] != Tree.BLOQUE:
            self.children.append(self.__load_child("DOWN", 0, 1))

    def __load_child(self, movement, dx, dy):

        x = self.x + dx
        y = self.y + dy
        cost = 0
        if self.mapa[x][y] == Tree.ESPACIO_VACIO:
            cost += 1
        elif self.mapa[x][y] == Tree.MONEDA:
            cost += 2
            self.find_coin = True
        elif self.mapa[x][y] == Tree.SIN_ROSTRO:
            cost += 2
            if self.find_coin:
                self.find_coin = False
                cost -= 5
        elif self.mapa[x][y] == Tree.HAKU:
            cost += 1
            self.end = True
        mapa = deepcopy(self.mapa)
        mapa[self.y][self.x] = Tree.ESPACIO_VACIO
        mapa[y][x] = Tree.CHIHIRO
        depth = self.depth + 1
        cost += self.cost
        return Tree(movement, self, mapa, x, y, depth, cost)

    def __str__(self):
        # print("Posicion:", self.x, self.y)
        # print("Mapa:")
        # for line in self.mapa: print(line)
        string = self.movement + "\n"
        string += "POSITION: " + str(self.x) + " " + str(self.y) + "\n"
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
                    temporal_line.append(int(char))
                width += 1
            mapa.append(temporal_line)
            heigth += 1
        self.mapa = mapa


tree_father = Tree("map/map1.txt")
tree_father.load_children()
for children in tree_father.children:
    print(children)
# tree_children = Tree("derecha" ,tree_father, tree_father.mapa, 1, 2, 1, 2)
