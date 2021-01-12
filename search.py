from tree import Tree


def bfs():
    root = Tree("map/map1.txt")
    qeue = list()
    qeue.append(root)

    # Mientras no esté vacío
    while qeue:

        node = qeue[0]

        # print(node.depth)
        if node.end:
            print("\n")
            print(node)
            return node

        node.load_children()
        qeue.extend(node.children)

        qeue.remove(node)

    return "No se ha encontrado una solución"
