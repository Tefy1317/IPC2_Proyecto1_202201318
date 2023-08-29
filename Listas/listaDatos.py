from Listas.nodoDato import*

class listaDatos: 
    def __init__(self):
        self.Inicio = None
        self.contadorDatos = 0
        pass

    def insertarDato(self, dato): 
        if self.Inicio is None: 
            self.Inicio = nodoDato(dato = dato)
            self.contadorDatos += 1
            return
        actual = self.Inicio
        while actual.siguiente: 
            actual = actual.siguiente
        actual.siguiente = nodoDato(dato = dato)
        self.contadorDatos += 1

    def imprimirListaDatos(self): 
        print("--"*40)
        actual = self.Inicio
        while actual != None: 
            print("Tiempo: "+str(actual.dato.tiempo)+" Amplitud: "+str(actual.dato.amplitud)+" Dato: "+str(actual.dato.dato))
            actual = actual.siguiente
        print("--"*40)