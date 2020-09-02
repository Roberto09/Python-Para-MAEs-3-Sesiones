def main():
    
    # 6.1 Estatutos de repetición para programación iterativa.
    # For Loops

    n = 10
    # range(start, end, increment)  donde se itera en el rango [start, end)
    # valores por default: range(start = 0, end, increment = 1)
    for i in range(0, n, 1):
        print(i)
        
    # Se simplifica a:
    for i in range(n):
        print(i)

    for i in range(5, n, 1):
        print(i)
        
    # Se simplifica a:
    for i in range(5, n):
        print(i)
        
    for i in range(0, n, 3):
        print(i)
    
    for i in range(n, 0, -1):
        print(i)

    
    # 7.1 Datos estructurados: Listas, Matrices, Strings, Diccionarios y Sets
    
    # Listas
    # Creacion de listas:
    mi_lista = []
    mi_lista2 = [1.5, 2.2, 4.8]
    mi_lista3 = ["hola", "esto es", "una lista"]
    mi_lista4 = [1.5, "prueba", True, 123]
    print(mi_lista4)
    
    # Inicializacion usando list comprehension
    mi_lista5 = [i*10 for i in range(4, 20, 2)]
    print(mi_lista5)
    
    # Indexing (0...size-1)
    print(mi_lista3[0])
    print(mi_lista3[1])
    print(mi_lista3[2])
    
    # Metodos comunes: append, insert, pop, reverse, sort
    # len -> nos dice el tamaño de una lista
    
    # len
    print(len(mi_lista4))

    # append
    mi_lista2.append(123.4)
    print(mi_lista2)
    mi_lista2.append(56.78)
    print(mi_lista2)
    
    # insert
    mi_lista3.insert(0, "prueba")
    print(mi_lista3)
    mi_lista3.insert(2, "otra prueba")
    print(mi_lista3)

    # pop
    mi_lista3.pop(2)
    print(mi_lista3)
    mi_lista3.pop(0)
    print(mi_lista3)
    
    # reverse
    print(mi_lista5)
    mi_lista5.reverse()
    print(mi_lista5)
    
    # sort
    print(mi_lista2)
    mi_lista2.sort()
    print(mi_lista2)
    
    # iterando en lista por index
    for i in range(len(mi_lista5)):
        print(mi_lista5[i] * 10 - 5)
        
    # iterando en lista por elemento
    for num in mi_lista5:
        print(num * 10 - 5)
        
    # Slicing lists [start:end]
    print("original: ", mi_lista5)
    print(mi_lista5[1:3])
    print(mi_lista5[1:])
    print(mi_lista5[:3])
    
    
    # Matriz -> lista de listas
    # Creacion de matrices:
    mi_matriz = [[2, 2, 1, 4],
                 [1, 5, 8, 9],
                 [2, 1, 3, 4]]

    # Esa matriz tiene 3 filas y 4 columnas. Es de tamaño 3 x 4
    print(mi_matriz)
    
    # len
    print(len(mi_matriz))
    
    # Indexing
    print(mi_matriz[0])
    print(mi_matriz[1])
    
    # Iterando por index
    for row in range(len(mi_matriz)):
        for col in range(len(mi_matriz[row])):
            print("matriz en ", row, ", ", col, " es: ", mi_matriz[row][col])
    
    # Iterando por elemento
    for row_list in mi_matriz:
        for num in row_list:
            print("num: ", num)
    
    # Utilizando metodos de listas en listas individuales de matrices
    mi_matriz[1].reverse()
    print(mi_matriz)

    # 7.1.3 Strings
    # Creacion de strings
    mi_string = "Hola! este es un string"
    mi_string2 = 'Hola! este es otro string'
    
    # Metodos comunes: find, lower, upper, replace, split
    # len -> tamaño de string
    
    # len
    print(len(mi_string))
    
    # find
    print(mi_string.find('e'))
          
    # lower
    print(mi_string)
    mi_string = mi_string.lower()
    print(mi_string)
    
    # upper
    print(mi_string)
    mi_string = mi_string.upper()
    print(mi_string)
    
    # replace
    print(mi_string)
    mi_string = mi_string.replace('ESTE', 'AQUEL')
    print(mi_string)
    
    # split
    palabras = mi_string.split(' ')
    print(type(palabras))
    print(palabras)
    
    # concatenation
    nuevo_string = mi_string + ' ' + mi_string2
    print(nuevo_string)
    
    print(mi_string)
    mi_string += ' text extra que podemos concatenar'
    print(mi_string)
    
    # splits
    print(mi_string[5:10])
    
    # Iterar sobre string por index
    for i in range(len(mi_string)):
        print("Caracter ", i, ": ", mi_string[i])
    
    # Iterar sobre string por caracter
    for caracter in mi_string:
        print("El caracter es: ", caracter)

if __name__ == '__main__':
    main()