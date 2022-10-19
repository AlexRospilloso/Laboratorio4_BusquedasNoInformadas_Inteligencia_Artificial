import random
import time


class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = None
        self.set_hijo(hijo)

    def set_hijo(self, hijo):
        if (hijo is not None):
            self.hijos.append(hijo)
            if self.hijos is not None:
                for h in self.hijos:
                    h.padre = self

    def get_hijos(self):
        return self.hijos

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado

    def __str__(self):
        return str(self.get_datos())


def bpa(estado_inicio, estado_solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodos_frontera.append(nodo_inicio)
    '''Creamos una lista_costos que inicialmente tendrá un solo valor que será 0, puesto que si el nodo_inicio es igual al estado_solución, no se
    tendrá hacer una búsqueda y la solución ya estaría planteada desde el inicio'''
    lista_costos = [0]

    while resuelto == False and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0)
        '''Al igual que con los nodos, sacaremos el costo en la posición 0 de la lista_costos para que desaparezca de la lista porque el nodo que
        contenía dicho costo también fue sacado de la lista frontera'''
        lista_costos.pop(0)
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            for i in range(len(estado_inicial)-1):
                hijo_datos = nodo_actual.get_datos().copy()
                temp = hijo_datos[i]
                hijo_datos[i] = hijo_datos[i + 1]
                hijo_datos[i + 1] = temp
                hijo = Nodo(hijo_datos)

                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodo_actual.set_hijo(hijo)
                    nodos_frontera.append(hijo)
                    '''Creamos una variable costo que será el párametro que le pasaremos a la función set_costo del hijo para que así esté vacío.
                    A partir de ello, primero verificamos si el valor no es None, porque puede ser que ya tenga un valor costo y ya no será
                    necesario aplicarle uno'''
                    costo = random.randrange(1,5)
                    if hijo.get_costo() == None:
                        hijo.set_costo(costo)
                        '''Añadimos el costo que creamos a la lista_costos. En cada iteración se crea un hijo y su costo y cada uno es llevado a su
                        respectiva lista y en el mismo indice'''
                        lista_costos.append(costo)

            '''Creamos un indice con un valor de 0 que es el que irá ordenando listas. Se irá resetenado porque en cada creación de hijos, los costos
            también aumentarán y se deben volver a ordenar las listas. Primero ordenará la lista_costos y, en base a ello,
            se ordenarán los nodos_frontera. Creamos listas auxiliares que nos servirtán para manipular el orden sin perder los datos de las
            listas originales'''
            indice = 0
            nodos_frontera_auxiliar = []
            lista_costos_auxiliar = []
            '''Hacemos un for inverso (para ordenar de mayor a menor) para los costos y dentro de este, añadimos otro ciclo for que se encargará de
            comprobar en la lista_costos. Si se da este caso, entonces añadimos el costo en la posición encontrada a la lista auxiliar y como
            mencionabamos que el indice de cada costo pertence a su igual en los nodos_forntera, se tomará la posición de los nodos_frontera y se
            añadirá el nodo a la otra lista auxiliar'''
            for i in range (4,0,-1):
                for j in range(len(lista_costos)):
                    if i == lista_costos[j]:
                        lista_costos_auxiliar.append(lista_costos[j])
                        nodos_frontera_auxiliar.append(nodos_frontera[j])
            '''Tras ordenar ambas listas auxiliares, ahora la lista_costos puede tomar los valores de la lista_costos_auxiliar y lo mismo con los
            nodos_frontera, y nos aseguramos de que no existan perdidas de valores'''
            lista_costos = lista_costos_auxiliar
            nodos_frontera = nodos_frontera_auxiliar



if __name__ == "__main__":
    '''El tiempo que tarda el programa es variable, puesto que al asignar costos aleatorios a los nodos y ordenarlos de mayor a menor respecto a
    dicho costo, es muy incierto el hecho de que el nodo con más probabilidad de encontrar la solución este en la primera posición para examinarlo
    con la función pop(0). Puede que en ciertas ocasiones este cerca del principio de la lista_frontera, realizando una búsqueda rápida; o que
    esté en el extremo final, haciendo que la búsqueda se vuelva exhaustiva y por ende, la resolución del problema tienda a demorar. La máxima
    cantidad de fichas que se puede tener para ejecutarse es indefinido, pues como ya vimos antes, el proceso de resolución del rompecabezas es
    un proceso aleatorio, pues puede que el nodo solución este en el principio de la lista frontera o al final, todo acorde a su costo asignado'''
    estado_inicial = [7, 6, 5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4, 5, 6, 7]
    start = time.time()
    nodo_solucion = bpa(estado_inicial, solucion)
    end = time.time()

    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print("Tiempo empleado ",end-start," segundos")
    print(resultado)