import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from Listas.nodoMatrizFinal import*
from Datos.matrizFinal import*

import os
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
            print("Grupo: "+str(actual.matrizFinal.grupoF)+" Amplitud: "+str(actual.matrizFinal.amplitudF)+" Suma Tuplas: "+str(actual.matrizFinal.sumValor))
            actual = actual.siguiente 
        print("")
        print("--"*30)
    
    def crearGraficaMatrizReducida(self, amplitud):
        f = open('archivo.dot','w')
        actual = self.Inicio
        grupo = actual.matrizFinal.grupoF
        text = f"""digraph G {{
            root [label = "Reducida = {actual.matrizFinal.nombre}"]
            filas [label = "A = {amplitud}"]
            columnas [label = "grupo= {grupo}"] 
            root -> filas
            root -> columnas
            """         
        marcaFilas = actual.matrizFinal.grupoF
        filaActual = 0 
        columnaActual = 0
        while actual: 
            if marcaFilas != actual.matrizFinal.grupoF:
                marcaFilas = actual.matrizFinal.grupoF
                columnaActual = 0 
                filaActual +=1       
            nombreNodo = f"celda_{filaActual}_{columnaActual}"
            text += f'   {nombreNodo} [label="{actual.matrizFinal.sumValor}"]\n'

            if filaActual == 0:
                text+= f'  root -> {nombreNodo}\n'
            else: 
                nodoSiguiente = f"celda_{filaActual-1}_{columnaActual}"
                text += f'   {nodoSiguiente} -> {nombreNodo}\n'
            actual = actual.siguiente
            columnaActual +=1
        text += """}"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng archivo.dot -o gr_MatrizReducida.png')
        print("GRAFICA GENERADA CON EXITO :) ")
    
    def generarXml(self):
        actual = self.Inicio
        amplitud = actual.matrizFinal.amplitudF
        root = ET.Element("señalesReducidas")
        senalXml = ET.SubElement(root,"senal", nombre = actual.matrizFinal.nombre, A = amplitud)
        grupo=ET.SubElement(senalXml,"grupo")

        my_data=ET.tostring(root)
        my_data=str(my_data)
        arbol_xml=ET.ElementTree(root)
        arbol_xml.write("salida.xml",encoding="UTF-8",xml_declaration=True)
    