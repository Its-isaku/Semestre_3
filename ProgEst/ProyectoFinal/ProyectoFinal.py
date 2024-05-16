#librerisas
import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, messagebox
#from cProfile import label
#from sys import maxsize


#funciones
def salir():
    messagebox.showinfo("Adios!", "Hasta luego gracias por comprar con nosotros!")
    VBoletos.destroy()





#creando ventana principal
VBoletos = tk.Tk()

#estilos




#Parametros de ventana principal
VBoletos.geometry("600x700")
VBoletos.title("Venta de boletos de tren")
VBoletos.configure(bg = "#295f48")
VBoletos.resizable(width = False, height = False)
VBoletos.iconbitmap("C:\\Users\\Isai\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\IconoVentana.ico")

#Logo principal
imagen1 = tk.PhotoImage(file = "C:\\Users\\Isai\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\trenlogo.png")
sublogo = imagen1.subsample(2)
logo = tk.Label(VBoletos, bg = "#295f48", image = sublogo)
logo.place(relx = 0.35, rely = 0.05)

#bordes decorativos
imagen2 = tk.PhotoImage(file = "C:\\Users\\Isai\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\derecho.png")
subBorde1 = imagen2.subsample(2)
BordeDerecho = tk.Label(VBoletos, bg = "#295f48", image = subBorde1)
BordeDerecho.place(relx = 0.0, rely = 0.0)

imagen3 = tk.PhotoImage(file = "C:\\Users\\Isai\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\izquierdo.png")
subBorde2 = imagen3.subsample(2)
BordeIzquierdo = tk.Label(VBoletos, bg = "#295f48", image = subBorde2)
BordeIzquierdo.place(relx = 0.79, rely = 0.0)

#botones para iniciar compras o para salir
salir = ttk.Button(VBoletos, text = "salir",command = salir)
salir.place(relx = 0.05, rely = 0.05)


#cerrando ventana principal
VBoletos.mainloop()
