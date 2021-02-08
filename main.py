import search
import utilities
import InterfazGrafica
from tree import Tree

#print("-----------------A*----------------------")
#utilities.init(search.a)
#print("----------------Profundidad---------------")
#utilities.init(search.bfs)
#print("----------------Costo uniforme------------")
#utilities.init(search.costo_uniforme)

nodo = search.a()
#a = nodo.mapa

b = nodo.calculate_nodo()

InterfazGrafica.viajeChihiro(b)
#print(a)
#print("")
#print(b[-1])

