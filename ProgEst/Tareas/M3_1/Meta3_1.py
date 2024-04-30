from tkinter import *
#Importa la libreria para poder crear ventanas
from tkinter import ttk
#Importas un submodulo para crear widgets como botones

#Funcion para abrir nueva ventana
def AbrirNuevaVentana():
    Nueva_Ventana = Toplevel(ventana)
    Nueva_Ventana.geometry('300x200')
    Nueva_Ventana.title('Nueva ventana')
    Label(Nueva_Ventana, text = "Hola mundo!").place(relx = .20, rely =.20)

ventana = Tk()
#se inicia la creacoin de una ventana 

ventana.geometry('500x400')
#se le especifica las dimensiones de la ventana

ventana.title ('Ejemplo de ventana')
#se le agrega un titulo al marco de la ventana

ventana.configure(bg = 'tomato')
#se le agrega un color de fondo a la ventana

#crear boton que mande a segunda ventana
boton = Button(ventana, text ="Click me", command = AbrirNuevaVentana).place(relx = .20, rely =.20)

ventana.mainloop()
#se usa para escificar que aqui termina la ventana 