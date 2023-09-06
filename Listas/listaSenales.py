from Listas.nodoSenal import* 
from Datos.grupos import*
from Listas.listaPatron import*
from Listas.listaMatrizReducida import*
from Datos.suma import*
from Listas.listaDatos import*
from Listas.listaNomGrupos import*
from Datos.nomGrupos import*
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

    def vaciarListas(self):
        self.Inicio = None

    def imprimirListaSenales(self):
        print("")
        print("***"*30)
        actual = self.Inicio
        while actual != None: 
            print("Nombre: "+actual.senal.nombre+" noFilas: "+str(actual.senal.filas)+" noColumnas: "+str(actual.senal.columnas))
            print(" ")
            print("DATOS OBTENIDOS")
            actual.senal.listaDatos.imprimirListaDatos()
            print("MATRIZ BINARIA")
            actual.senal.listaPatronDatos.imprimirListaDatos()
            actual = actual.siguiente
            print("")
        print("***"*30)
        print("")
        print("")
        
    def Eliminar(self, tiempo):
        actual = self.Inicio 
        anterior = None
        while actual and actual.senal.filas != tiempo: 
            anterior = actual 
            actual = actual.siguiente
        if anterior is None: 
            self.Inicio = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None


    def imprimirNoSenales(self):
         print("--"*20)
         print("Total de señales procesadas: "+str(self.contadorSenales))
         print("--"*20)

    def calcularPatrones(self):
        actual = self.Inicio
        while actual != None:
            actual.senal.listaPatronSenal = actual.senal.listaPatronDatos.mostrarPatrones(actual.senal.listaPatronSenal)
            actual.senal.listaPatronSenal.ImprimirListaPatron()
            listaPatronTemp = actual.senal.listaPatronSenal
            gruposRevisar = listaPatronTemp.encontrarPatrones()
            print("NUEVOS GRUPOS = "+gruposRevisar)
            cadenaAlmacenada = ""
            #gruposRevisar = 1,2,5,--3,4,--
            listaNomGruposTemp = listaNomGrupos()
            for digito in gruposRevisar: 
                if digito.isdigit() or digito == ",":
                        cadenaAlmacenada += digito
                elif digito == "-" and cadenaAlmacenada != "":
                        serieGrupo = actual.senal.listaDatos.mostrarSerieGrupo(cadenaAlmacenada)
                        listaNomGruposTemp.InsertarDato(nomGrupo= nombreGrupos(cadenaAlmacenada))
                        amplitud = actual.senal.columnas
                        actual.senal.listaAgrupaciones.InsertarDato(grupo = Grupos(actual.senal.nombre, cadenaAlmacenada, amplitud, serieGrupo))  
                        cadenaAlmacenada = ""
                else: 
                        cadenaAlmacenada = ""
            actual.senal.listaAgrupaciones.ImprimirListaGrupos()
            #listaNomGruposTemp.ImprimirListaNomGrupos()
            actual = actual.siguiente
        return
    
    def graficarListaOriginal(self, nombreSenalUsuario):
            actual = self.Inicio
            while actual != None: 
                if actual.senal.nombre == nombreSenalUsuario:
                    dot = actual.senal.listaDatos.crearGraficaOriginal(actual.senal.nombre, str(actual.senal.filas), str(actual.senal.columnas))
                    return dot
                actual = actual.siguiente
