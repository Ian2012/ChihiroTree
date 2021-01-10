import threading
import time

from Tree import Tree


def busqueda_por_amplitud():
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


def animated_loading(process):
    while process.is_alive():
        chars = [".", "..", "...", "....", "....."]
        for char in chars:
            print('\r' + 'Processing' + char, end="")
            time.sleep(0.3)


loading_process = threading.Thread(target=busqueda_por_amplitud)
loading_process.start()
animated_loading(loading_process)
loading_process.join()
