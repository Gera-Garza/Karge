class TablaVars:

    def __init__(self):
        self.tabla = {}

    def add_var(self, nombre, tipo):
        self.tabla[nombre] = {
            'nombre': nombre,
            'tipo': tipo,
        }
        print(self.tabla[nombre])

    def clear_tabla(self):
        self.tabla = {}

    def find_var(self, var):
        return var in self.tabla

    def get_var(self, var):
        if self.find_var(var):
            return self.tabla[var]
        else:
            raise Exception(f"Error: No existe la variable {var}")
