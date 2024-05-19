                                                                    #Librerias necesarias para la ejecucion del programa
import tkinter as tk
import serial
import time
                                                                    #se declara la clase
class MotorControllerApp:
    def __init__(self, master):                                     #metodo constructor
        self.master = master                                        #es la ventana principal
        self.master.title("Control de Motor Paso a Paso")           #Titulo de la ventana

        self.arduino = serial.Serial('COM3', 9600, timeout=1)       #conexion de arduino a python por el puerto serial
        time.sleep(2)                                               #Esperar a que se establezca la conexión

        self.create_widgets()                                       #creary configura los botones, escalas, etiquetas de la interfaz grafica

    def create_widgets(self):
        self.btn_rotate_both = tk.Button(self.master, text="Rotar Horaria/Antihoraria", command=self.rotate_both)#se crea el boton
        self.btn_rotate_both.pack(pady=10)                           #posicion del boton

        self.speed_label = tk.Label(self.master, text="Velocidad (0-100):")#crea una etiqueta
        self.speed_label.pack()                                       #posicion en la ventana

        self.speed_scale = tk.Scale(self.master, from_=0, to=100, orient='horizontal')#crea una barra que ajusta la velocidad
        self.speed_scale.pack(pady=10)                                #posicion en la ventana

        self.btn_set_speed = tk.Button(self.master, text="Establecer Velocidad", command=self.set_speed)#Crea un boton que establece la velocidad
        self.btn_set_speed.pack(pady=10)                               #posicion en la ventana

        self.btn_rotate_90 = tk.Button(self.master, text="Rotar 90 grados", command=self.rotate_90)#crea un boton que rota 90 grados
        self.btn_rotate_90.pack(pady=10)                               #posicion de boton

    def rotate_both(self):                                              #Rota el motor 
        self.arduino.write(b'1')                                        #envia 1 byte hacia arduino

    def set_speed(self):                                                #establece la velocidad del motor
        speed = self.speed_scale.get()                                  #obtiene el valor de la barra deslizante
        command = f'2{speed}\n'                                         #comando que envia a arduino la velocidad elegida
        self.arduino.write(command.encode())                            #envia el comando a arduino en bytes

    def rotate_90(self):                                                #Rota 90 grados
        self.arduino.write(b'3')                                        #envia 3 byte hacia arduino

    def close(self):                                                    #cierra la conexion serial
        self.arduino.close()                                            #asegura que los recursos se liberen adecuadamente

if __name__ == "__main__":                                              #comprueba si el script esta siendo ejecutado directamente
    root = tk.Tk()                                                      #crea la ventana principal
    app = MotorControllerApp(root)                                      #se crea la instancia para que cree la ventana principal con toda su logica
    root.protocol("WM_DELETE_WINDOW", app.close)                        #maneja el evento de cerrar la ventana
    root.mainloop()                                                     #inicia el bucle principal de eventos Tkinter, manteniendo la ventana abierta
