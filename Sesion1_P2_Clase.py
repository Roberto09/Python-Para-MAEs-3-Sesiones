def es_un_alien(edad, continente, confesion_alien, es_capitan_america):
    if((confesion_alien == 'si')
       or (continente != 'america' and continente != 'europa')
       or ((edad > 150) and not (es_capitan_america == 'si'))):
        return True
    else:
        return False

def main():
    """
    edad = int(input("Dime tu edad: "))
    continente = input("Dime tu continente: ")
    confesion_alien = input("Eres un alien? (si, no): ")
    es_capitan_america = input("Eres capitan america? (si, no): ")
    
    # () ==, !=, >, >=, <, <=, is, is not, in, not in
    # not, and, or
    
    if(confesion_alien == 'si'):
        print('Eres un alien')
    elif(continente != 'america' and continente != 'europa'):
        print('Eres un alien')
    elif((edad > 150) and not (es_capitan_america == 'si')):
        print('Eres un alien')
    else:
        print('Eres un humano')
    
        
    if((confesion_alien == 'si')
       or (continente != 'america' and continente != 'europa')
       or ((edad > 150) and not (es_capitan_america == 'si'))):
        print('Eres un alien')
    else:
        print('Eres un humano')
    
        
    if(es_un_alien(edad, continente, confesion_alien, es_capitan_america)):
        print('Eres un alien')
    else:
        print('Eres humano')
    """
    
    # While, continue, break, indices
    """
    contador = 0
    while(contador < 10):
        print(contador)
        contador = contador + 1
    """
    
    # Ciclo que sume enteros positos que nos de el usuario
    total = 0
    n = int(input('Cuantos numeros voy a sumar? '))
    indice = 0 # nos dice en que numero de iteracion voy
    
    while(indice < n):
        num = int(input('Dame el numero ' ))
        indice += 1
        if(num == 0):
            continue
        if(num < 0):
            print('Solo se permiten numeros positivos')
            break
        total += num
        
    
    
    print(total)
    print('termine')
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    