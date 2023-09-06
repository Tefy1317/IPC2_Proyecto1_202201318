from Listas.nodoDato import*
from Datos.patron import*
import sys
import os

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
        
    def mostrarPatrones(self, listaPatronSenal):
        actual = self.Inicio
        nombreSenal = actual.dato.nombre
        refFila = actual.dato.tiempo
        refAmplitud = actual.dato.amplitud
        filaInicio = False
        guardarPatron = ""
        while actual != None:
            if  refFila!=actual.dato.tiempo:
                filaInicio=False
                listaPatronSenal.InsertarDato(Patron(nombreSenal, refFila,refAmplitud, guardarPatron))
                guardarPatron = ""
                refFila = actual.dato.tiempo
                refAmplitud = actual.dato.amplitud
    
            if filaInicio == False:
                filaInicio=True
                guardarPatron += str(actual.dato.dato)+"-"
            else:
                guardarPatron+=str(actual.dato.dato)+"-"
            actual = actual.siguiente

        listaPatronSenal.InsertarDato(Patron(nombreSenal, refFila, refAmplitud, guardarPatron))

        return listaPatronSenal
    
    def mostrarGrupos(self, listaAgrupaciones):
        actual = self.Inicio
        nombreSenal = actual.dato.nombre
        refFila = actual.dato.tiempo
        refAmplitud = actual.dato.amplitud
        filaInicio = False
        guardarPatron = ""
        while actual != None:
            if  refFila!=actual.dato.tiempo:
                filaInicio=False
                listaAgrupaciones.InsertarDato(Patron(nombreSenal, refFila, refAmplitud, guardarPatron))
                guardarPatron = ""
                refFila = actual.dato.tiempo
                refAmplitud = actual.dato.amplitud
    
            if filaInicio == False:
                filaInicio=True
                guardarPatron += str(actual.dato.dato)+"-"
            else:
                guardarPatron+=str(actual.dato.dato)+"-"
            actual = actual.siguiente

        listaAgrupaciones.InsertarDato(Patron(nombreSenal, refFila,refAmplitud, guardarPatron))

        return listaAgrupaciones

    def mostrarSerieGrupo(self, grupo):
        resultado = ""
        temporal = ""
        cadenaAlmacenada = ""
        for digito in grupo: 
            if digito.isdigit():
                cadenaAlmacenada += digito
            else: 
                temporal = ""
                actual = self.Inicio
                while actual != None:
                    #print(" Grup"+str(grupo)+" AMPLITUD LISTADATOS: "+str(actual.dato.amplitud))
                    if actual.dato.tiempo == int(cadenaAlmacenada):
                        temporal += str(actual.dato.dato)+","
                        
                    actual = actual.siguiente
                resultado += temporal+"\n"
                cadenaAlmacenada = ""
        return resultado 
    
    
    def crearGraficaOriginal(self, nombre, filas, columnas):
        f = open('archivo.dot','w')
        text = f"""digraph G {{
            root [label = "{nombre}"]
            filas [label = "t = {filas}"]
            columnas [label = "A = {columnas}"] 
            root -> filas
            root -> columnas
            """ 
        actual = self.Inicio
        marcaFilas = actual.dato.tiempo
        filaActual = 0 
        columnaActual = 0
        while actual: 
            if marcaFilas != actual.dato.tiempo:
                marcaFilas = actual.dato.tiempo
                columnaActual = 0 
                filaActual +=1       
            nombreNodo = f"celda_{filaActual}_{columnaActual}"
            text += f'   {nombreNodo} [label="{actual.dato.dato}"]\n'

            if filaActual == 0:
                text+= f'  root -> {nombreNodo}\n'
            else: 
                nodoSiguiente = f"celda_{filaActual-1}_{columnaActual}"
                text += f'   {nodoSiguiente} -> {nombreNodo}\n'
            actual = actual.siguiente
            columnaActual +=1
        text += """}}"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng archivo.dot -o gr_MatrizOriginal.png')
        print("GRAFICA GENERADA CON EXITO :) ")