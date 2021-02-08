import search
import utilities

print("-----------------A*----------------------")
utilities.init(search.a)
print("----------------Profundidad---------------")
utilities.init(search.bfs)
print("----------------Costo uniforme------------")
utilities.init(search.costo_uniforme)
nodo = search.a()

