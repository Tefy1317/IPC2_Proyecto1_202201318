from Listas.nodoPatron import*

class listaPatron: 
    def __init__(self):
        self.Inicio = None
        self.contadorPatrones = 0 
        pass

    def InsertarDato(self, patron): 
        if self.Inicio is None: 
            self.Inicio = nodoPatron(patron = patron)
            self.contadorPatrones += 1
            return
        actual = self.Inicio
        
        while actual.siguiente: 
            actual = actual.siguiente
        actual.siguiente = nodoPatron(patron = patron)
        self.contadorPatrones += 1
    def ImprimirListaPatron(self):
        print("")
        print("--"*30)
        actual = self.Inicio
        print("PATRONES ENCONTRADOS EN SEÑAL: "+actual.patron.nombre)
        print("")
        while actual != None: 
            print("Tiempo: "+str(actual.patron.tiempo)+" Patron: "+actual.patron.seriePatron)
            actual = actual.siguiente 
            print("")
        print("")
        print("--"*30)
    
    def eliminarPatron(self, tiempo):
        actual = self.Inicio 
        anterior = None
        while actual and actual.patron.tiempo != tiempo: 
            anterior = actual 
            actual = actual.siguiente
        if anterior is None: 
            self.Inicio = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None

    def encontrarPatrones(self):
        resultado = ""
        while self.Inicio: 
            actual = self.Inicio
            amplitudTemp = ""
            tiempoTemp = ""
            #Almacena Tiempo
            while actual: 
                if actual.patron.seriePatron == self.Inicio.patron.seriePatron: 
                    tiempoTemp += str(actual.patron.tiempo)+","
                actual = actual.siguiente

            cadenaAlmacenada = ""
            for digito in amplitudTemp: 
                if digito.isdigit():
                    cadenaAlmacenada += digito
                else: 
                    if cadenaAlmacenada != "":
                        self.eliminarPatron(int(cadenaAlmacenada))
                        cadenaAlmacenada = ""
                    else: 
                        cadenaAlmacenada = ""

            cadenaAlmacenada = ""
            for digito in tiempoTemp: 
                if digito.isdigit():
                    cadenaAlmacenada += digito
                else: 
                    if cadenaAlmacenada != "":
                        self.eliminarPatron(int(cadenaAlmacenada))
                        cadenaAlmacenada = ""
                    else: 
                        cadenaAlmacenada = ""
            resultado += tiempoTemp+"--"
        return resultado
    




