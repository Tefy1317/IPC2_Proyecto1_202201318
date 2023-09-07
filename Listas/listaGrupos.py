import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from Listas.nodoGrupos import*
from Listas.listaMatrizReducida import*
from Datos.grupos import*
from Datos.suma import*
import sys
import os

class listaGrupos: 
    def __init__(self):
        self.Inicio = None
        self.contadorGrupos = 0 
        pass

    def InsertarDato(self, grupo): 
        if self.Inicio is None: 
            self.Inicio = nodoGrupos(grupo = grupo)
            self.contadorGrupos += 1
            return
        actual = self.Inicio
        
        while actual.siguiente: 
            actual = actual.siguiente
        actual.siguiente = nodoGrupos(grupo= grupo)
        self.contadorGrupos += 1

    def ImprimirListaGrupos(self):
        #print("")
        #print("*"*30)
        actual = self.Inicio
        listaMatrizTemp = listaMatrizReducida()
        sumaDatos = 0
        numeroActual = ""
        while actual != None: 
            amplitud = actual.grupo.amplitud
            serieGrupo = actual.grupo.serieGrupo
            nombreSenal = actual.grupo.nombre
            #print("NOMBRE PRUEBA: "+nombreSenal)
            #print("AMPLITUD: "+str(amplitud))
            #46,52,0,2
            grupo = actual.grupo.grupo
            for digito2 in serieGrupo:
                if digito2.isdigit():
                    #print("DIGITO2: "+str(digito2))
                    numeroActual += digito2
                elif digito2 == ",":
                    if numeroActual: 
                        listaMatrizTemp.InsertarDato(suma = Suma(nombreSenal, grupo,amplitud,numeroActual))
                        numeroActual = ""
            if numeroActual:
                listaMatrizTemp.InsertarDato(suma = Suma(nombreSenal, grupo,amplitud,numeroActual))
            actual = actual.siguiente 
        listaMatrizTemp.ImprimirListaMatrizR()
        

        
        
   
    
            