import xml.etree.ElementTree as ET
from Datos.senal import*
from Datos.dato import*
from Listas.listaDatos import*
from Listas.listaSenales import*
from Listas.listaPatron import*
from Listas.listaGrupos import*
os.system('cls')
opcion = 0 
#Menú
while(opcion != 7):
    print("*"*60) 
    print("Proyecto 1 - Introducción a la Programación 2")
    print("*"*60) 
    print("1. Cargar archivo")
    print("2. Procesar archivo")
    print("3. Escribir archivo salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar gráfica")
    print("6. Inicializar sistema")
    print("7. Salir")
    print("Ingrese una opción: ")
    opcion = int(input())

    if opcion == 1:
        print("--"*30)
        print("CARGAR ARCHIVO")
        print("--"*30)
        
        ruta = input("Ingrese ruta de archivo a cargar: ")
        #ruta = "C:\IPC2_Proyecto1_202201318\Entrada-Ejemplo.xml"
        if ruta != "":
            archivoCargado = ET.parse(ruta)
            print(" ")  
            print("--"*30)
            print("ARCHIVO CARGADO CORRECTAMETE")
            print("--"*30)
            print(" ")
            print(" ")
        else:
            print("NO SE HA CARGADO NINGUN ARCHIVO")
        
        pass
    elif opcion == 2: 
        print("--"*30)
        print("PROCESAR ARCHIVO")
        print("--"*30)
        if ruta == "":
            print("NO SE HA CARGADO NINGUN ARCHIVO")
        else: 
            Raiz = archivoCargado.getroot()
            listaSenalesInicial = listaSenales()

            for elementos in Raiz.findall('senal'):
                nombreSenal = elementos.get('nombre')
                filasSenal = elementos.get('t')
                columnasSenal = elementos.get('A')
                
                if int(filasSenal) > 0 and int(filasSenal) <= 3600: 
                    if int(columnasSenal) > 0 and int(columnasSenal) <= 30:
                        print(" ")
                        print("> Guardando datos cargados...")
                        print(" ")
                        listaDatosIncial = listaDatos()
                        listaPatronDatos = listaDatos()
                        listaPatronTemp = listaPatron()
                        listaGruposTemp = listaGrupos()
                    
                        for datos in elementos.findall('dato'):
                            tiempo = datos.get('t')
                            amplitud = datos.get('A')
                            datoX = datos.text
                            nuevoDato = Dato(nombreSenal, int(tiempo), int(amplitud), int(datoX))
                            listaDatosIncial.insertarDato(nuevoDato)
                            
                            if int(datoX) != 0: 
                                nuevoDato = Dato(nombreSenal, int(tiempo), int(amplitud), 1)
                                listaPatronDatos.insertarDato(nuevoDato)
                            else: 
                                nuevoDato = Dato(nombreSenal, int(tiempo), int(amplitud), 0)
                                listaPatronDatos.insertarDato(nuevoDato)
                        print(" ")
                        print("> Calculando Matriz Binaria...")
                        print(" ")
                        listaSenalesInicial.insertarDato(Senal(nombreSenal, int(filasSenal), int(columnasSenal), listaDatosIncial, listaPatronDatos, listaPatronTemp, listaGruposTemp))
                        listaSenalesInicial.imprimirNoSenales()
                    else: 
                        print("++"*30)
                        print("LA SEÑAL: "+nombreSenal+" FUE RECHAZADA POR A: "+columnasSenal)
                        print("++"*30)
                else:
                    print("++"*30)
                    print("LA SEÑAL: "+nombreSenal+" FUE RECHAZADA POR t: "+filasSenal)
                    print("++"*30)

            listaSenalesInicial.imprimirListaSenales()
            listaSenalesInicial.calcularPatrones()
        pass
    elif opcion == 3: 
        print("--"*30)
        print("ESCRIBIR ARCHIVO SALIDA")
        print("--"*30)
        
        root = ET.Element("señalesReducidas")
        tree = ET.ElementTree(root)
        with open("archivo.xml", "wb") as file:
            tree.write(file, encoding="utf-8", xml_declaration=True)

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
        nombreSenalUsuario = input("Ingrese el nombre de la señal que quiere graficar:")
        listaSenalesInicial.graficarListaOriginal(nombreSenalUsuario)
    elif opcion == 6:
        print("--"*30)
        print("INICIALIZAR SISTEMA")
        print("--"*30)
        listaSenalesInicial.Eliminar(int(filasSenal))
        ruta = ""
        print("SISTEMA INICIALIZADO CORRECTAMENTE...")
    elif opcion == 7:
        print("SALIENDO...")
        break