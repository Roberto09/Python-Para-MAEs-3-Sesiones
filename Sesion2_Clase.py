def main():
    # For loops
    n = 5
    
    # range(start, end, increment) donde se itera en el rango [start, end)
    # valores por default: range(start = 0, end, increment = 1)
    # 1 parametro range(end)
    # 2 parametros range(start, end)
    # 3 parametros range(start, end, increment)
    
    """
    total = 0
    for i in range(n):
        num = int(input('numero: '))
        total += num
    
    print(total)
    
    
    for i in range(5, 10):
        print(i)
    
    for i in range(0, 20, 3):
        print(i)
        
    # Ciclo alrevez
    for i in range(n, 0, -1):
        print(i)
    
    for i in range(n):
        print('hola') 
    """
    """
    # Listas
    mi_lista = []
    mi_lista1 = [1.7, 1.5, 1.8, 1.9]
    mi_lista2 = ["hola", "esto", "es", "una", "lista"]
    
    #            0     1         2     3
    mi_lista3 = [1.5, "prueba", True, 123]
    
    # len
    print(len(mi_lista1))
    
    # append
    mi_lista3.append(5.20)
    
    # insert
    print(mi_lista3)
    mi_lista3.insert(1, "elemento")
    print(mi_lista3)
    
    # pop
    print(mi_lista3)
    mi_lista3.pop(1)
    print(mi_lista3)
    
    # reverse
    print(mi_lista2)
    mi_lista2.reverse()
    print(mi_lista2)
    
    # sort
    print(mi_lista1)
    mi_lista1.sort()
    print(mi_lista1)
    """
    #Matrices -> lista de listas -> lista de filas de matriz
    
    matriz = [[2, 2, 1, 4],
              [1, 5, 8, 9],
              [2, 1, 3, 4]]
    
    filas = len(matriz) # 3
    columnas = len(matriz[0]) # 4
    print('filas: ', filas)
    print('columnas: ', columnas)
    
    print(matriz[1][2])
    
    total = 0
    for fila in range(filas):
        for columna in range(columnas):
            print('fila: ', fila, '  columna: ', columna, ' -> ', matriz[fila][columna])
            total += matriz[fila][columna]
            for ...
            
    print('La suma de todos los elementos de la matriz es: ', total)
    
    
    
if __name__ == '__main__':
    main()