from Listas.nodoMatrizReducida import*
from Datos.suma import*
from Listas.listaMatrizFinal import*
class listaMatrizReducida: 
    def __init__(self):
        self.Inicio = None
        self.contador = 0 
        pass

    def obtenerTamanoMatriz(self):
        return self.contador

    def InsertarDato(self, suma): 
        if self.Inicio is None: 
            self.Inicio = nodoMatrizR(suma = suma)
            self.contador += 1
            return
        actual = self.Inicio
        
        while actual.siguiente: 
            actual = actual.siguiente
        actual.siguiente = nodoMatrizR(suma = suma)
        self.contador += 1        

    def ImprimirListaMatrizR(self):
        print("")
        print("**"*30)
        print("  > Calculando Matriz Reducida...")
        print("**"*30)
        #-------------------------------------------        
        mgrupo = self.Inicio
        nomGrupo =mgrupo.suma.grupo
        yarecorriogrupo =0
        nombreSenal = mgrupo.suma.nombre        
        #-------------------------------------------
        listaFinal = listaMatrizFinal()
        sumaValor=0
        while mgrupo != None:            
            # EVALUA PRIMERO  SI YA SE PROCESO EL GRUPO CON yarecorriogrupo==1
            if yarecorriogrupo==1 and nomGrupo!=mgrupo.suma.grupo:
                yarecorriogrupo=0
                nomGrupo=mgrupo.suma.grupo                
            else:
                nomGrupo=mgrupo.suma.grupo
            #print("*CICLO nomGrupo="+nomGrupo+" valor mgrupo.suma.grupo="+str(mgrupo.suma.grupo)+" valor de yarecorriogrupo="+str(yarecorriogrupo))
            if nomGrupo == mgrupo.suma.grupo and yarecorriogrupo==0:
                yarecorriogrupo=1
                #print(" entro al GRUPO "+str(mgrupo.suma.grupo))
                #-------------------------------------------
                actual = self.Inicio
                grupo = actual.suma.grupo                        
                amplitud = actual.suma.amplitud                
                #-------------------------------------------                
                for i in range(1,amplitud+1):
                    actual = self.Inicio
                    contador=0
                    sumaValor=0                    
                    #print(" valI "+str(i))
                    while actual != None:
                        contador+=1 #aqui asignar AMPLITUD.
                        #print("DETALLEGrupo: "+str(actual.suma.grupo)+" Amplitud: "+str(i)+" Suma Tuplas: "+str(actual.suma.valor))                    
                        if contador == i and nomGrupo == actual.suma.grupo:
                            sumaValor+=int(actual.suma.valor)
                        if contador == amplitud:
                            contador=0                            
                        actual = actual.siguiente
                    listaFinal.InsertarDato(matrizFinal= MatrizFinal(nombreSenal, nomGrupo, i, sumaValor))
                    #print("")
                #print("")
                #print("AA"*30)
            mgrupo=mgrupo.siguiente      
        listaFinal.ImprimirListaMatrizReducidaFinal()
        listaFinal.crearGraficaMatrizReducida(amplitud)
        #listaFinal.generarXml()
