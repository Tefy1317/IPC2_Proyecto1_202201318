from Listas.nodoSenal import* 

class listaSenales: 
    def __init__(self):
        self.Inicio = None
        self.contadorSenales = 0
        pass
    def insertarDato(self, senal): 
        if self.Inicio is None: 
            self.Inicio = nodoSenal(senal = senal)
            self.contadorSenales += 1
            return
        actual = self.Inicio
        
        while actual.siguiente: 
            actual = actual.siguiente
        actual.siguiente = nodoSenal(senal = senal)
        self.contadorSenales += 1

    def imprimirListaSenales(self):
        print("")
        print("***"*30)
        actual = self.Inicio
        while actual != None: 
            print("Nombre: "+actual.senal.nombre+" noFilas: "+str(actual.senal.filas)+" noColumnas: "+str(actual.senal.columnas))
            actual.senal.listaDatos.imprimirListaDatos()
            actual.senal.listaPatronDatos.imprimirListaDatos()
            actual = actual.siguiente
            print("")
        print("***"*30)
        print("")
        print("")

    def imprimirNoSenales(self):
         print("--"*20)
         print("Total de señales cargadas: "+str(self.contadorSenales))
         print("--"*20)
    