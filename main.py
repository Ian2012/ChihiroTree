class Tree:

    def __init__(self, *args):
        if len(args) == 1:
            self.movement = "Root"
            self.father = None
            self.mapa = list()
            self.x = int()
            self.y = int()
            self.depth = 0
            self.cost = 0

            self.load_file(args[0])
            self.children = list()
            print(self.x, self.y)

            for line in self.mapa:
                print(line)
        else:
            self.father = args[0]
            self.mapa = args[1]
            self.x = args[2]
            self.y = args[3]
            self.depth = args[4]
            self.cost = args[5]

    def load_children(self):
        pass

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
tree_children = Tree(tree_father, tree_father.mapa, 1, 3, 1, 2, "derecha")
print(tree_children.cost)
