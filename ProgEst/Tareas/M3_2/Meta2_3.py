#Libreria de interfaz grafica
from tkinter import *
from tkinter import ttk

#funciones
def Suma():
    result = int(a.get()) + int(b.get())
    #mostrando resultado
    text_result.config(text="" + str(result))

def resta():
    result = int(a.get()) - int(b.get())
    text_result.config(text="" + str(result))

def multiplicacion():
    result = int(a.get()) * int(b.get())
    text_result.config(text="" + str(result))

def exit():
    #saliendo de la calculadora
    calculadora.destroy()

#creando ventana
calculadora = Tk()

#creadndo parametros
calculadora.geometry("400x300")
calculadora.title("Calculadora Basica")
calculadora.configure(bg="#387E71")
#img = PhotoImage(file='D:\\Coding\\ProgEst\Tareas\\M3_2\\calculadora.png')
#calculadora.iconphoto(False, img)
calculadora.resizable(width=False, height=False)

#creando labels y entradas
num1 = Label(text='Numero 1: ').place(relx=.05, rely=.05)
a = Entry(justify=CENTER)
a.place(relx=.35, rely=.05)

num2 = Label(text='Numero 2: ').place(relx=.05, rely=.15)
b = Entry(justify=CENTER)
b.place(relx=.35, rely=.15)

text3 = Label(text='Resultado:').place(relx=.05, rely=.25)
text_result = Label(text="   ")
text_result.place(relx=.35, rely=.25)

#creando botones
suma = Button(text='Suma', command=Suma, bg = "#075748", fg = "White").place(relx=.05, rely=0.85)
resta = Button(text='Resta', command=resta, bg = "#075748", fg = "White").place(relx=.18, rely=0.85)
multi = Button(text='Multiplicacion', command=multiplicacion, bg = "#075748", fg = "White").place(relx=.30, rely=0.85)
salir = Button(text='Salir', command=exit, bg = "tomato", fg = "white").place(relx=.55, rely=0.85)

#fin de la calculadora
calculadora.mainloop()
