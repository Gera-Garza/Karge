class memoria():
    def __init__(self):
        self.memoria = {}

    def enteros(self):
        ent = []

    def ent_temp(self):
        ent_temp = []

    def flotantes(self):
        flota = []

    def flot_temp(self):
        flot_temp = []

    def constantes(self):
        # los caracteres seran representados por numeros
        # el orden sera el siguiente
        # ,   ;   =   (   )    {   }   [   ]   *   /   +   -
        # 31  32  33  34  35  36  37  38  39  40  41  42  43
        caracteres = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]

    def palReservadas(self):
        # las palabras reservadas seran representados por numeros
        # el orden sera el siguiente
        # int  float  char  string  &&  ||   <   >   ==  !=  read  print for while if else return
        # 1     2     3      4      5   6    7   8    9  10   11    12   13   14   15  16   17
        especiales = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17]
