from collections import deque
"""Funcion que recibe una lista como parametro y devuelve la suma  """
lista=[1,2,3,4,5,6]
def suma_lista(lista):
    suma=0
    for i in lista:
        suma=suma+i
    print("La suma de la lista es: ",suma)
#suma_lista(lista)

"""recibir una cadena y retornar el inverso"""
texto="python"
def inverso_palabra(cadena):
    queue=deque(cadena)
    for i in cadena:
        lista=[]
        new=[]
        lista.append(i)
        invertido=queue.pop()
        new.append(invertido)
        print(new)
inverso_palabra(texto)
