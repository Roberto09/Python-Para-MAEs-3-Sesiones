def pedir_mat_usuario():
    rows = int(input("Filas: "))
    columns = int(input("Columnas: "))

    mat = [[0 for i in range(rows)] for j in range(columns)]
    
    for r in range(rows):
        for c in range(columns):
            mat[i][j] = int(input("Dime ", i, ", ", j, " : "))
            
    return mat
    
def escribir_en_archivo(matriz, archivo):
    for fila in matriz:
        for elemento in fila:
            archivo.write(str(elemento) + ', ')

        archivo.write('\n')

def matmul(a, b):    
    rows_a, columns_a = len(a), len(a[0])
    rows_b, columns_b = len(b), len(b[0])
    
    if columns_a != rows_b:
        print ('La encripcion no se puede realizar!')
        return

    # Matriz de rows_a x columns_b
    res = [[0 for i in range(rows_a)] for j in range(columns_b)]

    for i in range(rows_a):
        for j in range(columns_b):
            for k in range(columns_a):
                res[i][j] += a[i][k] * b[k][j]
    
    return res

def main():
    m1 = [[0, 2, 8],
          [2, 2, 3],
          [1, 5, 9]]
    
    m2 = [[7, 5, 9],
          [2, 3, 4],
          [8, 1, 6]]
    
    """
    print("Hola Agente!")
    print("Matriz de datos: ")
    m1 = pedir_mat_usuario()
    
    print("Matriz de encripcion: ")
    m2 = pedir_mat_usuario()
    """
    
    print('Encriptando...')
    
    archivo = open('archivito.txt', 'w')

    res = matmul(m1, m2)
    escribir_en_archivo(res, archivo)
    
    print('Listo!')
    archivo.close()

if __name__ == '__main__':
    main()