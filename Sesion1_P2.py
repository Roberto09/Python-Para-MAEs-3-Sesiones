
def es_un_alien(edad, continente, confesion_alien, es_capitan_america):
    if(confesion_alien == 'si'
       or (continente != 'america' and continente != 'europa' and continente != 'africa' and continente != 'asia' and continente != 'onceania')
       or ((edad < 0 or edad > 150) and not es_capitan_america)):
        return True
    else:
        return False

def main():
    # 5. Pensamiento computacional en problemas que requieran estructuras de decisión.
    # 5.1 Expresiones con operadores relacionales y lógicos para definir condiciones.
    # 5.2 Estatutos de decisión para programación con condiciones.
    # 5.3 Solución de problemas que involucren estatutos condicionales.
    
    # Operadores logicos en python: ORDEN:
    # () ==, !=, >, >=, <, <=, is, is not, in, not in
    # not, and, or
    edad = int(input("Dime tu edad: "))
    continente = input("Dime, en que continente vives(america, europa, africa, asia u oceania)?: ")
    confesion_alien = input("Eres un alien? (si, no): ")
    es_capitan_america = (input("Eres el capitan america :O (True, False)? ") == "True")
    
    if(confesion_alien == 'si'):
        print("Es un alien!")
    elif(continente != 'america' and continente != 'europa' and continente != 'africa' and continente != 'asia' and continente != 'onceania'):
        print("Es un alien!")
    elif((edad < 0 or edad > 150) and not es_capitan_america):
        print("Es un alien!")
    else:
        print("Es un humano!")
        
        
    # simplificando...
    if(confesion_alien == 'si'
       or (continente != 'america' and continente != 'europa' and continente != 'africa' and continente != 'asia' and continente != 'onceania')
       or ((edad < 0 or edad > 150) and not es_capitan_america)):
        print("Es un alien!")
    else:
        print("Es un humano!")
        
    # aun mas simplificado...
    if(es_un_alien(edad, continente, confesion_alien, es_capitan_america)):
       print("Es un alien!")
    else:
        print("Es un humano!")
    
    # 6. Pensamiento computacional en problemas que requieran repeticiones.
    # 6.1 Estatutos de repetición para programación iterativa.
    
    # While, continue, break, indices
    
    # While (Suma de enteros)
    print("Suma de numeros enteros")
    total = 0
    n = input("Cuantos numeros voy a sumar?")
    i = 0
    while(i < n):
        x = int(input("Dame el numero " + str(i) + ": "))
        total += x
        i += 1
    
    print("La suma total es: ", total)
    
    # While (Suma de numeros enteros positivos [romper en caso de numeros negativos])
    print("Suma de numeros decimales positivos, cuando escribas un numero negativo se rompera el ciclo el numero")
    total = 0
    n = input("Cuantos numeros voy a sumar?")
    i = 0
    while(i < n):
        x = int(input("Dame el numero " + str(i) + ": "))
        if(x < 0):
            print(x, " es un numero negativo! ya no se sumara")
            break
        total += x
        i += 1
    
    print("La suma total es: ", total)
    
        
    # While (Suma de numeros decimales positivos)
    print("Suma de numeros decimales positivos, cuando escribas un numero negativo se ignorara el numero")
    total = 0
    num_actual = 1
    while(num_actual >= 0):
        num_actual = input("Dame un numero: ")
        if(num_actual < 0):
            continue
        total += num_actual
    
    # 6.2 Solución de problemas que involucren programación con estatutos de repetición.
    naves_tie, naves_millennium_falcon, naves_raddus = 0, 0, 0
    print("Queremos saber mas de ti!")
    
    n = input("Cuantas naves tienes?")
    while(naves_tie + naves_millenium_falcon + naves_raddus < n):
        tipo = int(input("Que tipo de nave es?: 1) tie, 2) millennium falcon, 3) raddus? "))
        cantidad = int(input("Cuantas tienes de ese tipo:O ?"))
        if(tipo == 1):
            naves_tie += cantidad
        elif(tipo == 2):
            naves_millenium_falcon += cantidad
        else:
            naves_raddus += cantidad
            
    print("Las naves tie son: ", naves_tie)
    print("Las naves millenium falcon son: ", naves_millenium_falcon)
    print("Las naves raddus son: ", naves_raddus)
    
    print("Gracias por la entrevista, hasta pronto!")


if __name__ == '__main__':
    main()