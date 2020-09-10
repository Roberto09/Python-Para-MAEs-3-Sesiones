import math

def formula_cuadratica(a, b, c, operacion_b):
    #  operacion_b -> "suma" o "resta"
    if(operacion_b == "suma"):
        x1 = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
        return x1
    else:
        x2 = (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
        return x2

def formula_cuadratica_simplificada(a, b, c):
    x1 = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
    return x1, x2


def main():
    # Variables y constantes
    NOMBRE_ENTRENADOR = input('Dame tu nombre entrenador Pokemon!')
    edad = int(input('Dame tu eded entrenador Pokemon!'))

    print('Hola ', NOMBRE_ENTRENADOR, ', tienes ', edad, ' años')
    
    print("Es momento de ayudar a Pikachu!")
    print("Introduce la ecuacion de tipo ax^2 + bx + c que describe las defensas de Charizard!")
    a = float(input("Dame a: "))
    b = float(input("Dame b: "))
    c = float(input("Dame c: "))
    
    # Operadores matematicos
    # Formula cuadratica (-b +- sqrt(pow(b, 2) - 4*a*c))/ (2*a)
    
    # Programacion modular
    x1, x2 = formula_cuadratica_simplificada(a, b, c)
    print("Pikachu ataca en los tiempos: ", x1, " y ", x2, " !")
   
if __name__ == '__main__':
    main()