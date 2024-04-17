import tkinter as tk
import threading
import serial
import time

# Conexión con Arduino
puerto_serie = serial.Serial('COM3', 9600)
time.sleep(2)

def leer_estado_botom():
    while True:
        estado_botom = puerto_serie.readline().strip().decode('utf-8')
        #Preorden
        if estado_botom == "A":
            canvas.create_oval(95,15,180,100, fill="green")
            time.sleep(1)
            canvas.create_oval(10, 205, 100, 125, fill="yellow")
            time.sleep(1)
            canvas.create_oval(200, 199, 290, 125, fill="blue")
            time.sleep(1)
        #Inorden
        elif estado_botom=="B":
            canvas.create_oval(10, 205, 100, 125, fill="yellow")
            time.sleep(1)
            canvas.create_oval(95,15,180,100, fill="green")
            time.sleep(1)
            canvas.create_oval(200, 199, 290, 125, fill="blue")
            time.sleep(1)
        #Postorden
        elif estado_botom == "C":
            canvas.create_oval(10, 205, 100, 125, fill="yellow")
            time.sleep(1)
            canvas.create_oval(200, 199, 290, 125, fill="blue")
            time.sleep(1)
            canvas.create_oval(95,15,180,100, fill="green")
            time.sleep(1)
        else:
            canvas.create_oval(95,15,180,100, fill="white")
            canvas.create_oval(10, 205, 100, 125, fill="white")
            canvas.create_oval(200, 199, 290, 125, fill="white")

def iniciar_lectura():
    threading.Thread(target=leer_estado_botom, daemon=True).start()

# Configuración de la ventana
root = tk.Tk()
width = 500
height = 500
root.geometry(f"{width}x{height}")
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

iniciar_lectura()
root.mainloop()  # Mantén la aplicación en funcionamiento
