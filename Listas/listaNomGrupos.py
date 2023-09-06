from Listas.nodolistaNomGrupos import*
from Datos.nomGrupos import*
class listaNomGrupos: 
    def __init__(self):
        self.Inicio = None
        self.contador = 0 
        pass

    def InsertarDato(self, nomGrupo): 
        if self.Inicio is None: 
            self.Inicio = nodoNomGrupos(nomGrupo= nomGrupo)
            self.contador += 1
            return
        actual = self.Inicio
        
        while actual.siguiente: 
            actual = actual.siguiente
        actual.siguiente = nodoNomGrupos(nomGrupo= nomGrupo)
        self.contador += 1        
        
    def ImprimirListaNomGrupos(self):
        print("")
        print("--"*30)
        print("GRUPOS")
        print("")
        actual = self.Inicio
        while actual != None: 
            print("Grupo: "+str(actual.nomGrupo.nomGrupo))
            actual = actual.siguiente 
        print("")
        print("--"*30)