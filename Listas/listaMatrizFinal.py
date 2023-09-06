from Listas.nodoMatrizFinal import*
from Datos.matrizFinal import*
class listaMatrizFinal: 
    def __init__(self):
        self.Inicio = None
        self.contador = 0 
        pass

    def InsertarDato(self, matrizFinal): 
        if self.Inicio is None: 
            self.Inicio = nodoMatrizFinal(matrizFinal= matrizFinal)
            self.contador += 1
            return
        actual = self.Inicio
        
        while actual.siguiente: 
            actual = actual.siguiente
        actual.siguiente = nodoMatrizFinal(matrizFinal= matrizFinal)
        self.contador += 1        

    def ImprimirListaMatrizReducidaFinal(self):
        print("")
        print("--"*30)
        actual = self.Inicio
        nombreSenal = actual.matrizFinal.nombre
        print("MATRIZ REDUCIDA DE SEÑAL: "+nombreSenal)
        print("")
        while actual != None: 
            print("Grupo Final : "+str(actual.matrizFinal.grupoF)+" Amplitud: "+str(actual.matrizFinal.amplitudF)+" Suma Final: "+str(actual.matrizFinal.sumValor))
            actual = actual.siguiente 
        print("")
        print("--"*30)