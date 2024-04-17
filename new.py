import tkinter as tk
import serial
import time
import threading

# Se conecta Arduino con Python
puerto_serie = serial.Serial('COM3', 9600)
time.sleep(2)

# Función para leer el estado del botón
def leer_estado_botom():
    while True:
        estado_botom = puerto_serie.readline().strip().decode('utf-8')
        if estado_botom == "A":
            canvas.create_oval(95, 15, 180, 100, fill="green")
            time.sleep(1)
            canvas.create_oval(10, 205, 100, 125, fill="yellow")
            time.sleep(1)
            canvas.create_oval(200, 199, 290, 125, fill="blue")
            time.sleep(1)
        elif estado_botom == "B":
            canvas.create_oval(10, 205, 100, 125, fill="yellow")
            time.sleep(1)
            canvas.create_oval(95, 15, 180, 100, fill="green")
            time.sleep(1)
            canvas.create_oval(200, 199, 290, 125, fill="blue")
            time.sleep(1)
        elif estado_botom == "C":
            canvas.create_oval(10, 205, 100, 125, fill="yellow")
            time.sleep(1)
            canvas.create_oval(200, 199, 290, 125, fill="blue")
            time.sleep(1)
            canvas.create_oval(95, 15, 180, 100, fill="green")
            time.sleep(1)
        else:
            canvas.create_oval(95, 15, 180, 100, fill="white")
            canvas.create_oval(10, 205, 100, 125, fill="white")
            canvas.create_oval(200, 199, 290, 125, fill="white")

# Función para leer el valor del potenciómetro
def leer_valor_potenciometro():
    linea_datos = puerto_serie.readline().decode().strip()
    valor_potenciometro = ""
    for char in linea_datos:
        if char.isdigit():
            valor_potenciometro += char
    if valor_potenciometro:
        return int(valor_potenciometro)
    return 0


# Función para actualizar la gráfica
def actualizar_grafica():
    valor_potenciometro = leer_valor_potenciometro()
    altura_barra = valor_potenciometro / 1024 * alto_lienzo
    lienzo.coords(barra, 10, alto_lienzo - altura_barra, 40, alto_lienzo)
    ventana.after(10, actualizar_grafica)

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Aplicación combinada")

# Configuración de la gráfica de barras
alto_lienzo = 200
ancho_lienzo = 50
lienzo = tk.Canvas(ventana, width=400, height=400, bg="white")
lienzo.pack()
ventana.geometry(f"{alto_lienzo}x{ancho_lienzo}")
barra = lienzo.create_rectangle(10, alto_lienzo, 40, alto_lienzo, fill="blue")

# Configuración del lienzo para los círculos
canvas = tk.Canvas(ventana, width=500, height=500)
canvas.pack()

# Iniciar lectura de estado del botón en un hilo aparte
threading.Thread(target=leer_estado_botom, daemon=True).start()

# Iniciar actualización de la gráfica
actualizar_grafica()

ventana.mainloop()  # Mantén la aplicación en funcionamiento
