import math

""" Temas Vistos en esta clase:

1. Introducción a la solución de problemas mediante programación.

2. Pensamiento computacional en problemas que involucran cálculos.
2.1 Estructura básica de un programa.
2.2 Variables, constantes y tipos de datos.
2.3 Expresiones con operadores aritméticos para describir fórmulas.
2.4 Construcción de programas que utilicen funciones predefinidas.
2.5 Solución de problemas que requieran el uso de fórmulas matemáticas.

3. Pensamiento computacional en programas que involucren programación modular.
3.1 Programación modular.
3.2 Construcción de funciones y métodos que requieren cálculos matemáticos

TAREA:
3.3 Solución de problemas que involucren programación modular.
"""


"""3.2 Construcción de funciones y métodos que requieren cálculos matemáticos."""
def formula_cuadratica(a, b, c, operacion_b):
    # formula cuadratica (-b +- sqrt(pow(b, 2) - 4*a*c))/ (2*a)
    if(operacion_b == "suma"):
        return (-b + math.sqrt(pow(b, 2) - 4*a*c)) / (2*a)
    else:
        return (-b - math.sqrt(pow(b, 2) - 4*a*c)) / (2*a)
    
def formula_cuadratica_simplificada(a, b, c):
    x1 = (-b + math.sqrt(pow(b, 2) - 4*a*c))/ (2*a)
    x2 = (-b - math.sqrt(pow(b, 2) - 4*a*c))/ (2*a)
    return x1, x2 

"""2.1 Estructura básica de un programa."""
def main():
    
    """2.2 Variables, constantes y tipos de datos."""
    # Esta es una constante
    NOMBRE_ENTRENADOR = str(input("Dame tu nombre de entrenador Pokemon! "))
    
    # Esta es una variable
    edad_entrenador = int(input("Dame tu edad entrenador: "))
    
    print("Hola ", NOMBRE_ENTRENADOR, ", tienes: ", edad_entrenador, " años!")
    
    # Tipos de datos
    PI = 3.1416
    num_a = -4 #int
    num_b = 10.2 #float
    texto = "mensaje de texto" #string
    
    print("Tipo numero_a: ", type(num_a))
    print("Tipo numero_b: ", type(num_b))
    print("Tipo texto: ", type(texto))
    
    """2.3 Expresiones con operadores aritméticos para describir fórmulas."""
    
    # Operadores matematicos comunes : [ *, /, +, -, (), pow(a, b), sqrt(a)]
    a, b, c, d = 1.5, 4, 2.5, 3.2
    resultado_operacion = (a + c) * b + d
    print(resultado_operacion)

    """2.4 Construcción de programas que utilicen funciones predefinidas.
    2.5 Solución de problemas que requieran el uso de fórmulas matemáticas.
    """
    
    # Formula cuadratica (-b +- sqrt(pow(b, 2) - 4*a*c))/ (2*a)
    a, b, c = 1.0, 6.0, 8.0
    x1 = (-b + math.sqrt(pow(b, 2) - 4*a*c))/ (2*a)
    x2 = (-b + math.sqrt(pow(b, 2) - 4*a*c))/ (2*a)
    
    print("x1: ", x1)
    print("x2: ", x2)
    
    """3.1 Programación modular."""
    
    print("Es momento de ayudar a Pikachu!")
    print("Introduce la ecuacion de tipo ax^2 + bx + c que describe las defensas de Charizard: ")
    
    # Pedimos input
    a = float(input("Dame a: "))
    b = float(input("Dame b: "))
    c = float(input("Dame c: "))
    
    # Simplificacion de lo anterior utilizando formulas
    x1 = formula_cuadratica(a, b, c, "suma");
    x2 = formula_cuadratica(a, b, c, "resta");
    print("x1: ", x1)
    print("x2: ", x2)
    
    # Pedimos input denuevo
    a = float(input("Dame a: "))
    b = float(input("Dame b: "))
    c = float(input("Dame c: "))
    
    # Simplificamos aun mas lo anterior
    x1, x2 = formula_cuadratica_simplificada(a, b, c)
   
    print("Pikachu debe atacar en los tiempos: ", x1, " y ", x2, " !")
    
if __name__ == "__main__":
    main()