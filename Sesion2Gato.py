def gano_horizontal(mtrx, simb):
    rows, columns = 3, 3
    
    for r in range(rows):
        hay_ganador = True
        
        for c in range(columns):
            if mtrx[r][c] != simb:
                hay_ganador = False
                break
        
        if hay_ganador:
            return True

    return False

def gano_vertical(mtrx, simb):
    rows, columns = 3, 3
    
    for c in range(columns):
        hay_ganador = True
        
        for r in range(rows):
            if mtrx[r][c] != simb:
                hay_ganador = False
                break
        
        if hay_ganador:
            return True

    return False

def gano_diag_principal(mtrx, simb):
    rows = 3
    for i in range(rows):
        if mtrx[i][i] != simb:
            return False
        
    return True



def gano_diag_inv(mtrx, simb):
    rows = 3
    for i in range(rows):
        if mtrx[i][rows-1-i] != simb:
            return False
        
    return True
    
def gano_alguien(mtrx, simb):
    if(gano_vertical(mtrx, simb)
       or gano_horizontal(mtrx, simb)
       or gano_diag_principal(mtrx, simb)
       or gano_diag_inv(mtrx, simb)):
        return True   
 
    return False

def imprimir_tablero(mtrx):
    for i in range(3):
        for j in range(3):
            print(mtrx[i][j], end = ' ')
        print('')

def jugar_gato():
    mtrx = [['*', '*', '*'],
            ['*', '*', '*'],
            ['*', '*', '*']]
    
    mtrx = [[4, 0, 5],
            [3, 8, 1],
            [2, 0, 9]]

    imprimir_tablero(mtrx)
    turno_j1 = True
    for turno in range(9):
        # primero imprimimos el tablero
        # revisamos de quien es turno
        if(turno_j1):
            print('Turno de j1')
        else:
            print('Turno de j2')
        
        # pedimos datos hasta que nos den una posicion valida
        pos_valida = False
        while not pos_valida:
            simb, pos_i, pos_j = input("Dime tu figura y posicion: ").split()
            pos_i = int(pos_i)
            pos_j = int(pos_j)
            
            if mtrx[pos_i][pos_j] == '*':
                mtrx[pos_i][pos_j] = simb
                pos_valida = simb
                
        imprimir_tablero(mtrx)
        # si gano alguien entonces lo imprimimos y terminamos programa
        if(gano_alguien(mtrx, simb)):
            print ("Ganaron las: ", simb, " !")
            return
    
    # Ocurrio un empate! :/
    imprimir_tablero(mtrx)
    print('Emapte!')


def main():
    print('Hola bienvenid@ a el juego del gato. Comencemos!')
    jugar_gato()

if __name__ == '__main__':
    main()