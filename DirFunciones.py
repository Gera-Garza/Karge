import TablaVars


class dirFunc():
    def __init__(self):
        self.dirFunciones = {}

    def añadeFn(self, NomFun, TipoFun, TipoRtn, ListaPar=[]):
        self.dirFunciones[NomFun] = {
            'tipo': TipoFun,
            'nombre': NomFun,
            'tipoReturn': TipoRtn,
            'var': TablaVars(),
        }

    def existeFun(self, NomFun):
        if NomFun in self.dirFunciones.keys():
            return True
        else:
            return False

    def getFun(self, nomFun):
        if existeFun(nomFun):
            return self.dirFunciones[nomFun]
        else:
            print("Error:No existe la función")
            return None
