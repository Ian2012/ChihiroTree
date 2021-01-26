from dataclasses import dataclass, field
from queue import PriorityQueue
from typing import Any

from tree import Tree


def bfs():
    root = Tree("map/map1.txt")
    qeue = list()
    qeue.append(root)

    while qeue:
        node = qeue[0]
        if node.end:
            print("\n\n", node)
            return node

        node.load_children()
        qeue.extend(node.children)

        qeue.remove(node)

    return "No se ha encontrado una solución"


def a():
    root = Tree("map/map1.txt")
    qeue = PriorityQueue()
    qeue.put(PrioritizedItem(root.f(), root))

    while qeue:
        node = qeue.get().item
        if node.end:
            print("\n\n", node)
            return node

        node.load_children()
        for child in node.children:
            qeue.put(PrioritizedItem(child.f(), child))


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)
