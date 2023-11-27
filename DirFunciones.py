import TablaVars


class DirFunciones():
    def __init__(self):
        self.dirFunciones = {}

    def addFun(self, nombre, tipoReturn,dirInicio,recursos,TablaVars,tipoParams):
        self.dirFunciones[nombre] = {
            'nombre': nombre,
            'tipoReturn': tipoReturn,
            "dirInicio": dirInicio,
            'Recursos': recursos,
            'var': TablaVars(),
            'TipoParams': tipoParams
        }
        print(self.dirFunciones[nombre])

    def existeFun(self, NomFun):
        return NomFun in self.dirFunciones

    def getFun(self, nomFun):
        if self.existeFun(nomFun):
            return self.dirFunciones[nomFun]
        else:
            print("Error:No existe la función")
            return None
