#Corto 1 - Proyectos

def fileAppend(fileName = 'collatz.txt'):

    #Si el archivo 'fileName' no existe, se crea uno nuevo con ese nombre.
    archivo = open(fileName,'a') #Abrir para agregar a archivo existente
    archivo.write('\n\nNuevo evento de append...\n')
    print('Espere, agregando datos al archivo...')

    numero = 10
    cont = 10
    lista = []
    for i in range(2,numero+1):
        var = i
        for j in range(0,cont):
            if var != 1:
                if var%2 == 0:
                    print("es par ",var)
                    var = var/2
                    lista.append(var)
                else:
                    print("no es par", var)
                    var = (3*var)+1   
                    lista.append(var)
            else:
                j = 100
                print("Lista: ",lista) 

    archivo.close() #Siempre cerrar el archivo al finalizar la escritura
    print('\n\nAppend finalizado')


        


