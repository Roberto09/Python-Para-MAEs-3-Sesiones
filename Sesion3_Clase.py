import os

def main():
    # Archivos
    # Abrir archivos: r : read, a : append, w : write, x : create
    # read -> lectura unicamente
    # append -> agrega al final del archivo
    # write -> reescribe archivo
    # create -> lo mismo que write pero si el archivo ya existe entonces truena el programa
    """
    archivo = open('archivito.txt','r')
    
    # Iterar por archivos
    for linea in archivo:
        print(linea)
        
    archivo.close()
    
    
    # Ejemplo de escritura
    archivo2 = open('archivito2.txt', 'w')
    mis_oraciones = ['hola como', 'estas este es', 'un grupo de palabras']
    
    for oracion in mis_oraciones:
        archivo2.write(oracion+'\n')
    """
        
    # revisar exitencia de un archivo
    if os.path.exists('archivito.txt'):
        print('El archivo si existe!')
    else:
        print('El archivo no existe!')
    
if __name__ == '__main__':
    main()