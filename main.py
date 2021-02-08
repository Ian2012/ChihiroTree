import InterfazGrafica
import search
import utilities

print("----------------Busqueda por amplitud---------------")
utilities.init(search.bfs)
print("----------------Costo uniforme------------")
utilities.init(search.costo_uniforme)
print("-----------------A*----------------------")
utilities.init(search.a)

InterfazGrafica.viajeChihiro(search.bfs().calculate_nodo(), "Busqueda por amplitud")
InterfazGrafica.viajeChihiro(search.costo_uniforme().calculate_nodo(), "Costo uniforme")
InterfazGrafica.viajeChihiro(search.a().calculate_nodo(), "A*")
