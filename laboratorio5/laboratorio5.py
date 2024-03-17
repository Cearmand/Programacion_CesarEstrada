import serial#Se importa el modulo serial para comunicacion
from serial.tools.list_ports import comports#lista los puertos series disponibles
from time import sleep#introduce pausas en el programa
from tkinter import *#tambien se utiliza tkinter para interfaces graficas

estadoLed = 0

def setup():#Inicialisa la comunicacion con el dispositivo serie
    global puerto
    puerto = serial.Serial(comports()[0].device, 9600)#se crea el objeto serial
    sleep(2)  # Espera a que se establezca la conexión

def draw():#dibuja los botones en una ventana grafica
    global estadoLed
    canvas.delete("all")#Borra todos los elementos dibujaos previamente en el lienzo
    if estadoLed == 1:
        #se crena los ovalos con colores, cuando se enciende el led
        canvas.create_oval(100,50,200,150, fill="red")
        canvas.create_oval(100,50,1,150, fill="green")
        canvas.create_oval(200,50,300,150, fill="blue")
    elif estadoLed == 0:
        #se crean los ovalos sin color, cuando se apaga el led
        canvas.create_oval(100,50,200,150, fill="#F4FFA5")
        canvas.create_oval(100,50,1,150, fill="#F4FFA5")
        canvas.create_oval(200,50,300,150, fill="#F4FFA5")
        


def mousePressed(event):#Es un evento que se ejecuta cuando se da clic
    global estadoLed
    if estadoLed == 0:#Si el led esta apagado entonces: 
        estadoLed = 1#Enciende el led
        puerto.write(b'1')#Escribe el byte 1 en el puerto serial hacia arduino para encender el led
    else:#Si el led esta encendido:
        estadoLed = 0#Apaga el led
        puerto.write(b'0')#Escribe el byte 0 en el puerto serial hacia arduino para apagar el led
    draw()

# Configuración de la ventana
root = Tk()
width = 500
height = 500
root.geometry(f"{width}x{height}")
canvas = Canvas(root, width=width, height=height)
canvas.pack()

setup()

canvas.bind("<Button-1>", mousePressed)

root.mainloop()  # Mantén la aplicación en funcionamiento