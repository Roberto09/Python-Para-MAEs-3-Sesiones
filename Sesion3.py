import os

def main():
    
    # 7.1.2 Matrices.
    # Repaso de matrices
    
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
    print(mi_matriz[0][0])
    print(mi_matriz[0])
    
    # Iterando por elemento
    for fila in mi_matriz:
        for num in fila:
            print(num, ', ')
        print('')
    
    
    # Iterando por index
    for row in range(len(mi_matriz)):
        for col in range(len(mi_matriz[row])):
            print("matriz en ", row, ", ", col, " es: ", mi_matriz[row][col])    

            
    # 7.1.3 Strings.
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
    
    # 8. Pensamiento computacional en problemas que involucran archivos.
    # 8.1 Creación y uso de archivos.
    # 8.2 Solución de problemas que involucren programación con archivos.
    
    # Abrir archivos
    # Modos de archivos : r : read, a : append, w : write, x : create
    archivo = open('archivito.txt', 'r')
    
    # Iterar por archivos
    for line in archivo:
        print(line)
    
    # Cerrar archivos
    archivo.close()
    
    archivo2 = open('archivito2.txt', 'w')
    mis_oraciones = ['hola como', 'estas este es', 'un grupo de palabras']
    
    for oracion in mis_oraciones:
        archivo2.write(oracion+'\n')
        
    # revisar existencia (debemos importar os -> import os)
    if os.path.exists('archivoX.txt'):
        print('El archivo si existe!')
    else:
        print('El archivo no existe!')
    
if __name__ == '__main__':
    main()