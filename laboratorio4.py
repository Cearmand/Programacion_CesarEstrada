from collections import deque
import time
# #Implementación de una Pila (Stack)
# #Se define la pila
pila=["Mario","Pedro","Juan","Lucas","Mateo"]
#           Funcion que agrega un elemeto a la pila
def añadir_elemento():
    pila.append(input("Ingrese un nuevo nombre: "))
    print(f"\n-Se añadio el nombre a la pila \n{pila}")
#           Funcion que elimina un elemeto de la pila
def eliminar_elemt():
    pila.pop()
    print(f"\n-Se elimino el ultimo nombre de la pila\n{pila}")
#           Funcion que imprime el elemento superior 
def elemto_superior():
    print(f"\n-El primer elemto de la pila\n{pila[0]}")
#           Funcion que invierte la fila con queue
def invertir_cola(A):
    newlist=[]
    queue=deque(A)
    while queue:
        invertido_A = queue.pop()
        newlist.append(invertido_A)
    print("Pila original",pila)
    print("Pila invertida",newlist)
#          Se llaman a las funciones
# añadir_elemento()    
# eliminar_elemt()
# elemto_superior()
# invertir_cola(pila)

# #Implementar una cola utilizando una lista en Python
cola=[1,2,3,4,5]
def enqueue():
    cola.append(int(input("Agragar un dato: ")))
    print("Dato agregado a la cola",cola)
def dequeue():
    cola.pop()
    print("Dato eliminado de la cola",cola)
def front():
    print("El primer dato de la cola es:",cola[0])
def atencion_al_cliente():
    queue = deque(cola)
    while queue:
        print("Atendiendo al cliente #",queue.popleft())
        time.sleep(1)
# enqueue()
# dequeue()
# front()
# atencion_al_cliente()

#Verificación de Paréntesis Balanceados
def verificacion_parentesis(cadena):
    stack=[]#definimos la pila
    for i in cadena:#recorremos la cadena de parantesis
        if i =="(":#verificamos si el primer caracter es un parentesis de apertura
            stack.append(i)#si el parentesis es de apertura, se agrega a la pila
        elif i==")":#Si el primer if no se comprueba pasa a este if y verifica si el caracter es un parentesis de cierre
            if len(stack)==0:#si la pila esta vacia eso quiere decir que el parentesis de cierre no tienen un parentesis de apertura por lo que se falso
                return False
            else:
                stack.pop()#si la pila no esta vacia se elimina el parentesis de apertura correspondiente del parentesis de apertura
    return len(stack)==0#se devuelve un true ya que la pila esta vacia correctamente segun las aperturas y cierres
cadena1="((()))"
cadena2="(()()"
cadena3=")))))"
# print(f"Primera cadena es: {verificacion_parentesis(cadena1)}")
# print(f"Segunda cadena es: {verificacion_parentesis(cadena2)}")
# print(f"Tercera cadena es: {verificacion_parentesis(cadena3)}")

#Implementación de una Cola con Dos Pilas
class ColaConPilas:
    #atributos
    def __init__(self):
        self.pilaIn=[]
        self.pilaOut=[]
    #metodo que agrega elementos a la lista de entrada
    def enqueue(self,elemt):
        self.pilaIn.append(elemt)
    #metodo que elimina elementos de la lista entrada y las guarda en la lista salida
    def dequeue(self):
        if not self.pilaOut:#El if evalua si la lista esta vacia 
            while self.pilaIn:#Mientras si hay elementos en la lista entrada se ejecuta el siclo
                self.pilaOut.append(self.pilaIn.pop())#se agrega a la lista salida los elementos eliminados de la lista entrada
        if not self.pilaOut:#Se evalua otravez para ver si la lista esta vacia y alertar que no hay nada en la lista salida
            print("La cola esta vacia")
            return None
        return self.pilaOut.pop()#Si la lista de salida tienen algun elemento, muestra solo el superior
    
cola= ColaConPilas()
cola.enqueue(10)
cola.enqueue(100)
cola.enqueue(800)
# print("Elemento eliminado:", cola.dequeue())
# print("Elemento eliminado:", cola.dequeue())
# print("Elemento eliminado:", cola.dequeue())
# print("Elemento eliminado:", cola.dequeue())

#Revertir la Mitad de una Cola
Cola=['a','b','c','d','e','f']
def revertir_mitad_cola(entrada_cola):
    revertido=[]
    mitad=len(entrada_cola)//2
    entrada_cola[mitad:]
    revertido.append(entrada_cola[:mitad])
    while entrada_cola[mitad:]:
        revertido.append(entrada_cola.pop())
    print("Cola inicial",entrada_cola,"\nCola partida a la mitad y revertida",revertido)
#revertir_mitad_cola(Cola)