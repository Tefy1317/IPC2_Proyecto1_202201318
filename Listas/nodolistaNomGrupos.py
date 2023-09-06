class nodoNomGrupos: 
    def __init__(self, nomGrupo = None, siguiente = None):
        self.nomGrupo = nomGrupo
        self.siguiente = siguiente 
        pass
    
    def devolverGrupos(self):
        return self.nomGrupo.nomGrupo