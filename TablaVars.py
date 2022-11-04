class TablaVars():

    def __init__(self):
        self.tabla = {}

    def addVar(self, tVar, nomV, dMem):
        self.tabla[nomV] = {
            'nombre': nomV,
            'tipo': tVar,
            'dirMem': dMem
        }
        print(self.tabla[nomV])

    def delTabla(self):
        self.tabla.clear()

    def findVar(self, Var):
        if Var in self.tabla.keys():
            return True
        else:
            return False

    def getVar(self, Var):
        if findVar(Var):
            return self.tabla[Var]
        else:
            print("Error: No existe la variable")
            return None
