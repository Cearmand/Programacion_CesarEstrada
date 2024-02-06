#1 variables y operadores aritmeticos
# num1=float(input("Ingrese el primer numero: "))
# num2=float(input("Ingrese el segundo numero "))
# print(f"SUMA: {num1+num2}\nRESTA:{num1-num2}\nMULTIPLICACIÓN:{num1*num2}\nDIVICIÓN: {round((num1/num2),2)}")

#2 Condicionales (if/else/elif) y Operadores Relacionales:
# try:
#     num=int(input("Ingrese un numero: "))
#     if num>0:
#         print("El numero es positivo.")
#     elif num<0:
#         print("El numero es negativo.")
#     else:
#         print("El numero es igual a cero.")
# except ValueError:    
#     print("Dato no valido")

#3. Ciclos (while/for) y Operadores Lógicos
# cont=1
# num=0
# while cont<=10:
#     num+=2
#     print(cont,") ",num)
#     cont+=1

#4 Funciones y Condicionales
# def par_impar(num1, num2):
#     suma=num1+num2
#     if suma%2==0:
#         print("El numero",suma,"es par por lo que es True")
#     else:
#         print("El numero",suma,"es impar por lo que es False")
    
# x=float(input("Ingrese el primer numero: "))
# x1=float(input("Ingrese el segundo numero: "))
# par_impar(x,x1)

#5 clases y metodos
# class Estudiante:
#     #atributos
#     def __init__(self,name, edad, nota):
#         self.name=name
#         self.edad=edad
#         self.nota=nota
#     def aprobacion(self):
#         if self.nota>=60:
#             print(f"El estudiante {self.name} con edad {self.edad} aprobo con {self.nota}")
#         else:
#             print(f"El estudiante {self.name} con edad {self.edad} reprobo con {self.nota}")
# #Crear objeto
# nombre=input("Ingrese su nombre: ")
# edadEstudiante=int(input("Ingrese su edad: "))
# calificacion=int(input("Ingrese la calificacion: "))
# estudiante = Estudiante(nombre,edadEstudiante,calificacion)
# #Llamar a la funcion
# estudiante.aprobacion()
