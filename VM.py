from parser import cuadruplos
def ejecutar_operacion(operador, operando1, operando2, resultado):
    # Lógica para ejecutar la operación según el cuádruplo
    if operador == '+':
        return operando1 + operando2
    elif operador == '-':
        return operando1 - operando2
    elif operador == '*':
        return operando1 * operando2
    elif operador == '/':
        return operando1 / operando2
    elif operador == '=':
        print(f'Asignación: {resultado} = {operando1}')



def leer_cuadruplos():
    for cuadruplo in cuadruplos:
        operador, operando1, operando2, resultado = cuadruplo
        resultado_operacion = ejecutar_operacion(operador, operando1, operando2, resultado)
        print(f'Resultado de la operación: {resultado_operacion}')

if __name__ == "__main__":
    leer_cuadruplos()