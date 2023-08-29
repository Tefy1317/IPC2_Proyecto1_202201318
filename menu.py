import xml.etree.ElementTree as ET
from Datos.senal import*
from Datos.dato import*
from Listas.listaDatos import*
from Listas.listaSenales import*

opcion = 0 
#Menú
while(opcion != 6):
    print("*"*60) 
    print("Proyecto 1 - Introducción a la Programación 2")
    print("*"*60) 
    print("1. Cargar archivo")
    print("2. Procesar archivo")
    print("3. Escribir archivo salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar gráfica")
    print("6. Salir")
    print("Ingrese una opción: ")
    opcion = int(input())

    if opcion == 1:
        print("--"*30)
        print("CARGAR ARCHIVO")
        print("--"*30)

        ruta = input("Ingrese ruta de archivo a cargar: ")
        archivoCargado = ET.parse(ruta)
        print(" ")
        print("--"*30)
        print("ARCHIVO CARGADO CORRECTAMETE")
        print("--"*30)
        print(" ")
        print(" ")
        pass
    elif opcion == 2: 
        print("--"*30)
        print("PROCESAR ARCHIVO")
        print("--"*30)
        Raiz = archivoCargado.getroot()
        listaSenalesInicial = listaSenales()
        for elementos in Raiz.findall('senal'):
            nombreSenal = elementos.get('nombre')
            filasSenal = elementos.get('t')
            columnasSenal = elementos.get('A')
            print(" ")
            print("Guardando datos cargados...")
            print(" ")
            listaDatosIncial = listaDatos()
            listaPatronDatos = listaDatos()

            for datos in elementos.findall('dato'):
                tiempo = datos.get('t')
                amplitud = datos.get('A')
                datoX = datos.text
                nuevoDato = Dato(int(tiempo), int(amplitud), int(datoX))
                listaDatosIncial.insertarDato(nuevoDato)
                
                if int(datoX) != 0: 
                    nuevoDato = Dato(int(tiempo), int(amplitud), 1)
                    listaPatronDatos.insertarDato(nuevoDato)
                else: 
                    nuevoDato = Dato(int(tiempo), int(amplitud), 0)
                    listaPatronDatos.insertarDato(nuevoDato)
            print(" ")
            print("Calculando Matriz Binaria...")
            print(" ")
            listaSenalesInicial.insertarDato(Senal(nombreSenal, int(filasSenal), int(columnasSenal), listaDatosIncial, listaPatronDatos))
            listaSenalesInicial.imprimirNoSenales()

        listaSenalesInicial.imprimirListaSenales()
        pass
    elif opcion == 3: 
        print("--"*30)
        print("ESCRIBIR ARCHIVO SALIDA")
        print("--"*30)
        pass
    elif opcion == 4: 
        print("--"*30)
        print("DATOS ESTUDIANTE")
        print("--"*30)
        print("> Estephanie Alejandra Ruiz Perez")
        print("> 202201318")
        print("> Introducción a la Programación 2 sección C")
        print("> Ingeniería en Ciencias y Sistemas")
        print("> 4to Semestre")
        pass
    elif opcion == 5: 
        print("--"*30)
        print("GENERAR GRÁFICA")
        print("--"*30)
    elif opcion == 6:
        print("SALIENDO...")
        break