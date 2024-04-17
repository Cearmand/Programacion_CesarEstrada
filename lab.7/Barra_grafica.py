import tkinter as tk
import serial
import time
import threading

#Se conecta arduino con python
puerto_serie = serial.Serial('COM3', 9600)
time.sleep(2)

#lee el estado del potencimetro
def leer_valor_potenciometro():
    linea_datos = puerto_serie.readline().decode().strip()#Lee el estado del potencimetro
    if linea_datos:#verifica si linea_datos tiene algun contenido dentro
        return int(linea_datos)
    return 0
#catualiza la grafica
def actualizar_grafica():
    valor_potenciometro =leer_valor_potenciometro()#se guarda el valor del potencimetro
    altura_barra = valor_potenciometro / 1024 * alto_lienzo#calcula la altura de la barra
    lienzo.coords(barra, 10, alto_lienzo - altura_barra, 40, alto_lienzo)#actualiza las coordenadas del rectangulo
    ventana.after(10, actualizar_grafica)#actualiza la grafica

ventana = tk.Tk()
ventana.title("Gráfica de Barras")

alto_lienzo = 200
ancho_lienzo = 50
lienzo = tk.Canvas(ventana, width=400, height=400, bg="white")
lienzo.pack()
ventana.geometry(f"{alto_lienzo}x{ancho_lienzo}")
#es la barra azul
barra = lienzo.create_rectangle(10, alto_lienzo, 40, alto_lienzo, fill="blue")


actualizar_grafica()
ventana.mainloop()