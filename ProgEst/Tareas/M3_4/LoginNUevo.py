#librerisas
import tkinter as tk
from tkinter import Toplevel, messagebox
from tkinter import ttk
from cProfile import label
from sys import maxsize
import random



#funciones
def salir():
    Login.destroy()

def Ventana2():

    global subimg2

    #creando dificultadoes para el juego matematico
    def Mododalidad():

        Modo_de_dificultad = dificultad_Combobox.get()

        if Modo_de_dificultad == "facil":
            messagebox.showinfo("Modo fácil", "Has seleccionado modo fácil.")
            num1 = random.randrange(1, 10)
            NumAleatorio1.config(text=str(num1))

            num2 = random.randrange(1, 10)
            NumAleatorio2.config(text="" + str(num2))


        elif Modo_de_dificultad == "medio":
            messagebox.showinfo("Modo medio", "Has seleccionado modo medio.")
            num1 = random.randrange(1, 100)
            NumAleatorio1.config(text=str(num1))

            num2 = random.randrange(1, 100)
            NumAleatorio2.config(text="" + str(num2))

        elif Modo_de_dificultad == "avanzado":
            messagebox.showinfo("Modo avanzado", "Has seleccionado modo avanzado.")
            num1 = random.randrange(1, 1000)
            NumAleatorio1.config(text=str(num1))

            num2 = random.randrange(1, 1000)
            NumAleatorio2.config(text="" + str(num2))

        else:
            messagebox.showerror("Selección de dificultad", "Por favor, selecciona una dificultad.")


    def generar_numeros():
        nivel = dificultad_Combobox.get()
        if nivel == "facil":
            num1 = random.randrange(1, 10)
            num2 = random.randrange(1, 10)
        elif nivel == "medio":
            num1 = random.randrange(1, 100)
            num2 = random.randrange(1, 100)
        elif nivel == "avanzado":
            num1 = random.randrange(1, 1000)
            num2 = random.randrange(1, 1000)
        else:
            messagebox.showerror("Selección de dificultad", "Por favor, selecciona una dificultad.")
            return

        NumAleatorio1.config(text=str(num1))
        NumAleatorio2.config(text=str(num2))
    
    #verificando la respuesta
    def verificar_respuesta():
        num1 = int(NumAleatorio1.cget("text"))
        num2 = int(NumAleatorio2.cget("text"))
        resultado_esperado = num1 + num2
        resultado_usuario = int(resultado.get())

        if resultado_usuario == resultado_esperado:
            messagebox.showinfo("Correcto", "¡Correcto!")
        else:
            messagebox.showerror("Incorrecto", "Incorrecto")

        # Generar nuevos números independientemente del resultado
        generar_numeros()

    def ev2():
        Login.deiconify()
        VentanaSec1.destroy()





    if password.get() !="" and user.get()!="":

        if user.get() == "Admin" and  int(password.get()) == 1234:

            Login.withdraw()
            VentanaSec1 = Toplevel()
            
            VentanaSec1.resizable(width = False, height = False)
            VentanaSec1.configure(bg = "#239B56")
            VentanaSec1.geometry('380x320')
            VentanaSec1.title('Sesion Admin')
            VentanaSec1.iconbitmap("C:\\Users\\Isai\\Desktop\\Coding\\ProgEst\\Tareas\\M3_4\\login.ico")

            #agregar imagen
            imagenVentanaa2 = tk.PhotoImage(file = "C:\\Users\\Isai\\Desktop\\Coding\\ProgEst\\Tareas\\M3_4\\imagenAdm.png")
            subimg2 = imagenVentanaa2.subsample(5)
            tk.Label(VentanaSec1, bg = "#239B56", image = subimg2).place(relx = 0.21, rely = 0.002)

            ttk.Label(VentanaSec1, text = "bienvenido Admin!",background = "#239B56" , style = "S3.TLabel").place(relx=0.15, rely=0.55)
            Regresar1 = tk.Button(VentanaSec1, text="Regresar", width= 10, height=2, command=ev2).place(relx=0.38, rely=0.75)





        elif user.get() == "Secretaria" and  int(password.get()) == 1234:
            Login.withdraw()
            VentanaSec1 = Toplevel()

            VentanaSec1.resizable(width = False, height = False)
            VentanaSec1.configure(bg = "#FF5733")
            VentanaSec1.geometry('380x320')
            VentanaSec1.title('Sesion Secretaria')

            #agregar imagen
            imagenVentanaa2 = tk.PhotoImage(file = "C:\\Users\\Isai\\Desktop\\Coding\\ProgEst\\Tareas\\M3_4\\secretaria.png")
            subimg2 = imagenVentanaa2.subsample(3)
            tk.Label(VentanaSec1, bg = "#FF5733", image = subimg2).place(relx = 0.25, rely = 0.002)

            ttk.Label(VentanaSec1, text = "bienvenida Secretaria!",background = "#FF5733" , style = "S3.TLabel").place(relx=0.095, rely=0.55)
            Regresar2 = tk.Button(VentanaSec1, text="Regresar", width= 10, height=2, command=ev2).place(relx=0.38, rely=0.75)
            




        elif user.get() == "Invitado" and  int(password.get()) == 1234:
            Login.withdraw()
            VentanaSec1 = Toplevel()

            VentanaSec1.resizable(width = False, height = False)
            VentanaSec1.configure(bg = "#FFA07A")
            VentanaSec1.geometry('380x320')
            VentanaSec1.title('Sesion Invitado')

            #agregar imagen
            imagenVentanaa2 = tk.PhotoImage(file = "C:\\Users\\Isai\\Desktop\\Coding\\ProgEst\\Tareas\\M3_4\\invitado.png")
            subimg2 = imagenVentanaa2.subsample(5)
            tk.Label(VentanaSec1, bg = "#FFA07A", image = subimg2).place(relx = 0.23, rely = 0.002)

            ttk.Label(VentanaSec1, text = "bienvenido Invitado!",background = "#FFA07A" , style = "S3.TLabel").place(relx=0.11, rely=0.55)
            Regresar3 = tk.Button(VentanaSec1, text="Regresar", width= 10, height=2, command=ev2).place(relx=0.38, rely=0.75)
            



        elif user.get() == "Juegos de matematicas" and  int(password.get()) == 1234:
            Login.withdraw()
            VentanaSec1 = Toplevel()

            VentanaSec1.configure(bg = "#DAF7A6")
            VentanaSec1.geometry('580x520')
            VentanaSec1.title('Sesion Juegos de matematicas')
            VentanaSec1.resizable(width = False, height = False)

            #texto de Bienvenida
            ttk.Label(VentanaSec1, text = "Juegos de habilidades matematicas!",background = "#DAF7A6" , style = "S4.TLabel").place(relx=0.047, rely=0.05)

            global dificultad_Combobox
            ttk.Label(VentanaSec1, text = "Selecciona Dificultad:",background = "#DAF7A6", style = "S5.TLabel").place(relx=0.044, rely=0.25)
            dificultad_Combobox = ttk.Combobox(VentanaSec1, values = ['facil', 'medio', 'avanzado'], font=('Comfortaa', 15), justify = "center",width = 10)
            dificultad_Combobox.place(relx=0.545, rely=0.26)

            #botton para regresar
            Regresar1 = tk.Button(VentanaSec1, text = "Regresar", font=('Comfortaa', 15), command=ev2)
            Regresar1.place(relx=0.24, rely=0.85)

            #boton para iniciar
            iniciar = tk.Button(VentanaSec1, text = "Iniciar",font=('Comfortaa', 12), command = Mododalidad)
            iniciar.place(relx=0.8, rely=0.255)

            #boton para verificar
            verificar = tk.Button(VentanaSec1, text = "Verificar", font=('Comfortaa', 15), command=verificar_respuesta)
            verificar.place(relx=0.53, rely=0.85)

            #crando secciones para difcultades
            
            NumAleatorio1 = ttk.Label(VentanaSec1, text = "",background = "white", width = 8, justify = "center", style = "S5.TLabel")
            NumAleatorio1.place(relx=0.05, rely=0.55)

            SignoMas = ttk.Label(VentanaSec1, text = "+",background = "#DAF7A6", style = "S5.TLabel")
            SignoMas.place(relx=0.27, rely=0.55)

            NumAleatorio2 = ttk.Label(VentanaSec1, text = "",background = "white", width = 8, justify = "center", style = "S5.TLabel")
            NumAleatorio2.place(relx=0.32, rely=0.55)

            SignoMas = ttk.Label(VentanaSec1, text = "=",background = "#DAF7A6", style = "S5.TLabel")
            SignoMas.place(relx=0.55, rely=0.55)

            resultado = tk.Entry(VentanaSec1, justify = "center", width = 10,font=('Comfortaa', 20))
            resultado.place(relx=0.60, rely=0.55)

                




            #crear entrys donde aparezcan los numeros que deberas sumar y un entry para poner la respuesta
            #si la respuesta es correcta, arrojar un messagebox con su respectivo mensaje
            #una vez se cierre el messagebox se generaran nuevos valores aleatorios 
            
            

    else:
        messagebox.showerror("error", "favor de ingresar las credenciales")






#creando ventana
Login = tk.Tk()

#creando estilos
estilo = ttk.Style()
estilo.configure("S1.TLabel", font=('Comfortaa', 80), background="#071b40", foreground="#e0e2d0")
estilo.configure("S2.TLabel", font=('Comfortaa', 35), background="#071b40", foreground="#e0e2d0")
estilo.configure("S3.TLabel", font=('Comfortaa', 25), foreground="#e0e2d0")
estilo.configure("S4.TLabel", font=('Comfortaa', 25), foreground="black")
estilo.configure("S5.TLabel", font=('Comfortaa', 20,"bold"), foreground="black")
estilo.configure("S1.TButton",font=('Comfortaa', 15), width=15, height=2, background = "black")

#parametros de la ventana
Login.geometry("600x600")
Login.title("Login v2")
Login.configure(bg = "#071b40")
Login.resizable(width = False, height = False)
Login.iconbitmap("C:\\Users\\Isai\\Desktop\\Coding\\ProgEst\\Tareas\\M3_4\\login.ico")

#agrego imagen
imagen1 = tk.PhotoImage(file = "C:\\Users\\Isai\\Desktop\\Coding\\ProgEst\\Tareas\\M3_4\\imagen2.png")
subimg = imagen1.subsample(12)
tk.Label(Login, bg = "#071b40", image = subimg).place(relx = 0.345, rely = 0.2)

#creando labels
ttk.Label(Login, text = "Login", style = "S1.TLabel").place(relx = 0.26, rely = 0.025)
ttk.Label(Login, text = "Users", style = "S2.TLabel").place(relx = 0.38, rely = 0.45)
ttk.Label(Login, text = "Password", style = "S2.TLabel").place(relx = 0.32, rely = 0.65)

#creando entradas
user = ttk.Combobox(Login, values = ['Admin', 'Secretaria', 'Invitado', 'Juegos de matematicas'], font=('Comfortaa', 15), justify = "center")
user.place (relx = 0.295, rely = 0.55)
password = tk.Entry(Login, show="*",justify = "center", width=30, font=('Comfortaa', 15))
password.place (relx = 0.225, rely = 0.75)

#creando botones
salir = ttk.Button(Login, text = "salir",command = salir, style = "S1.TButton").place(relx = 0.125, rely = 0.90)
login = ttk.Button(Login, text = "Login",command = Ventana2, style = "S1.TButton").place(relx = 0.560, rely = 0.90)


#cerrando ventana
Login.mainloop()