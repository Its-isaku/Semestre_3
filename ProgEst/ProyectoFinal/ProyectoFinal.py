import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, messagebox

# Variables globales para imágenes
global subBorde3, subBorde4, subBorde5, subBorde6, subBorde7, subBorde8, subBorde9, subBorde10

#funciones
def salir():
    messagebox.showinfo("Adios!", "Hasta luego gracias por comprar con nosotros!")
    VBoletos.destroy()

def VentaBoletos():
    VentanaEleccion = TipoBoleto.get()
    
    if VentanaEleccion == 'Viaje':

        global subBorde3, subBorde4, sublogo2

        def ev2():
            VBoletos.deiconify()
            VentanaSec1.destroy()

        
        def MontoEdad():

            global Mfinal

            if TipoEdades.get() == '':
                return None
            
            edad = TipoEdades.get()
            adulto = Adulto_var.get()

            if edad in ['5 - 15','16 - 18'] and adulto == "No":
                messagebox.showerror("Error", "Un adulto debe ir contigo!")
                return None

            if edad in ['5 - 15','16 - 18']:
                Mfinal = 40
            elif edad in ['19 - 29', '30 - 39']:
                Mfinal = 70
            elif edad == '40 - 60+':
                Mfinal = 45

            return True

        def MontoCantidad():

            global CantidadPersonas

            try:
                CantidadPersonas = int(TipoCantidad.get())
                return True
            except ValueError:
                messagebox.showerror("Error", "Ingresa un número válido para la cantidad de personas")
                return False

        def MontoFinal():

            MontoEdad()
            MontoCantidad()

            if MontoEdad() is None and MontoCantidad() is None:
                messagebox.showerror("Error!", "Debes completar los requerimientos")
                return

            def Parte1():

                global Mfinal

                if Mfinal is not None and CantidadPersonas is not None:
                    if Mfinal == 45 and CantidadPersonas >= 4:
                        return Mfinal * CantidadPersonas * (1 - 0.15)
                    elif Mfinal == 70 and CantidadPersonas >= 4:
                        return Mfinal * CantidadPersonas * (1 - 0.15)
                    elif Mfinal == 40 and CantidadPersonas >= 4:
                        return Mfinal * CantidadPersonas * (1 - 0.15)
                    else:
                        return Mfinal * CantidadPersonas
                else:
                    return 0
    
            def Parte2():

                tarifa = 0

                if inicio_var.get() == "" or destino_var.get() == "" or inicio_var.get() == destino_var.get():
                    messagebox.showerror("Error!", "Elige un inicio y destino válidos!")
                    return 0

                if inicio_var.get() == "Tecate" and destino_var.get() == "Tijuana":
                    tarifa = 30 
                elif inicio_var.get() == "Tecate" and destino_var.get() == "Mexicali":
                    tarifa = 40 
                elif inicio_var.get() == "Tecate" and destino_var.get() == "Ensenada":
                    tarifa = 50 
                elif inicio_var.get() == "Tecate" and destino_var.get() == "Rosarito":
                    tarifa = 50 
    
                elif inicio_var.get() == "Tijuana" and destino_var.get() == "Tecate":
                    tarifa = 30 
                elif inicio_var.get() == "Tijuana" and destino_var.get() == "Mexicali":
                    tarifa = 40 
                elif inicio_var.get() == "Tijuana" and destino_var.get() == "Ensenada":
                    tarifa = 50 
                elif inicio_var.get() == "Tijuana" and destino_var.get() == "Rosarito":
                    tarifa = 50
    
                elif inicio_var.get() == "Mexicali" and destino_var.get() == "Tijuana":
                    tarifa = 30 
                elif inicio_var.get() == "Mexicali" and destino_var.get() == "Tecate":
                    tarifa = 40 
                elif inicio_var.get() == "Mexicali" and destino_var.get() == "Ensenada":
                    tarifa = 50 
                elif inicio_var.get() == "Mexicali" and destino_var.get() == "Rosarito":
                    tarifa = 50
    
                elif inicio_var.get() == "Ensenada" and destino_var.get() == "Tijuana":
                    tarifa = 50 
                elif inicio_var.get() == "Ensenada" and destino_var.get() == "Mexicali":
                    tarifa = 50 
                elif inicio_var.get() == "Ensenada" and destino_var.get() == "Tecate":
                    tarifa = 50 
                elif inicio_var.get() == "Ensenada" and destino_var.get() == "Rosarito":
                    tarifa = 30 
    
                elif inicio_var.get() == "Rosarito" and destino_var.get() == "Tijuana":
                    tarifa = 50 
                elif inicio_var.get() == "Rosarito" and destino_var.get() == "Mexicali":
                    tarifa = 50 
                elif inicio_var.get() == "Rosarito" and destino_var.get() == "Ensenada":
                    tarifa = 30 
                elif inicio_var.get() == "Rosarito" and destino_var.get() == "Tecate":
                    tarifa = 50
                            
                return tarifa * CantidadPersonas
    
    
            M1 = Parte1()
            M2 = Parte2()
    
            total = M1 + M2
            texto6.config(text="$" + str(total))

            return total

        def Promos1():
            global subBorde6, subBorde5

            def ev3():
                VentanaSec1.deiconify()
                VentanaSec2.destroy()

            VentanaSec1.withdraw()
            VentanaSec2 = Toplevel()

            VentanaSec2.geometry('800x600')
            VentanaSec2.configure(bg = "#295f48")
            VentanaSec2.title('Compra de boletos')
            VentanaSec2.iconbitmap("C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\IconoVentana.ico")
            VentanaSec2.resizable(width = False, height = False)

            texto8 = ttk.Label(VentanaSec2, text="Sistema de cobro:", style="S1.TLabel")
            texto8.place(relx=0.23, rely=0.05)

            texto9 = ttk.Label(VentanaSec2, text="-----------------------------------------------------\n Para saber el monto total que se cobrará, \n primero se calcula cuánto se cobra cada\n boleto dependiendo de la edad del individuo\n después se suma el costo de cada boleto y\n se obtiene el valor total que será cobrado\n-----------------------------------------------------", style="S4.TLabel")
            texto9.place(relx=0.15, rely=0.15)

            texto10 = ttk.Label(VentanaSec2, text="Edades", style="S1.TLabel")
            texto10.place(relx=0.38, rely=0.5)

            texto11 = ttk.Label(VentanaSec2, text="------------------------\n De la edad 40 hacia\n adelante se hace un\n descuento del 15%\n------------------------", style="S4.TLabel")
            texto11.place(relx=0.33, rely=0.6)

            imagen7 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\derecho.png")
            subBorde5 = imagen7.subsample(3)
            BordeDerecho3 = tk.Label(VentanaSec2, bg="#295f48", image=subBorde5)
            BordeDerecho3.place(relx=0.0, rely=0.0)

            imagen8 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\izquierdo.png")
            subBorde6 = imagen8.subsample(3)
            BordeIzquierdo3 = tk.Label(VentanaSec2, bg="#295f48", image=subBorde6)
            BordeIzquierdo3.place(relx=0.89, rely=0.0)

            salir = tk.Button(VentanaSec2,
                            command=ev3,
                            background="#49ab81",
                            foreground="#18392b",
                            activebackground="#dcbb57",
                            activeforeground="#18392b",
                            highlightthickness=2,
                            highlightcolor="#dcbb57",
                            width=9,
                            height=1,
                            border=0,
                            font=('Arial', 16, 'bold'),
                            text="Salir",
                            )
            salir.place(relx=0.4, rely=0.9)

        if TipoBoleto.get() != "":

            if TipoBoleto.get() == "Viaje":

                def BoletoComprado():
                    global subBorde9, subBorde10

                    def ev5():
                        VentanaSec1.deiconify()
                        VentanaSec5.destroy()

                    CantidadBoletos = TipoCantidad.get()
                    InicioViaje = inicio_var.get()
                    DestinoViaje = destino_var.get()
                    HorarioViaje = TipoHorario.get()
                    Total = MontoFinal()
                    

                    VentanaSec1.withdraw()
                    VentanaSec5 = Toplevel()

                    VentanaSec5.geometry('400x600')
                    VentanaSec5.configure(bg="#295f48")
                    VentanaSec5.title('Recibo de Compra')
                    VentanaSec5.iconbitmap("C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\IconoVentana.ico")
                    VentanaSec5.resizable(width=False, height=False)

                    texto19 = ttk.Label(VentanaSec5, text="Recibo", style="S1.TLabel")
                    texto19.place(relx=0.3, rely=0.15)

                    texto20 = ttk.Label(VentanaSec5, text=f"------------------------------\nCantidad de boletos: {CantidadBoletos}\n", style="S4.TLabel")
                    texto20.place(relx=0.12, rely=0.23)

                    texto21 = ttk.Label(VentanaSec5, text=f"El viaje inicia en: {InicioViaje}\n", style="S4.TLabel")
                    texto21.place(relx=0.12, rely=0.32)

                    texto22 = ttk.Label(VentanaSec5, text=f"El viaje termina en: {DestinoViaje}\n", style="S4.TLabel")
                    texto22.place(relx=0.12, rely=0.38)

                    texto23 = ttk.Label(VentanaSec5, text=f"El Viaje inicia a las: {HorarioViaje}\n", style="S4.TLabel")
                    texto23.place(relx=0.12, rely=0.44)

                    texto24 = ttk.Label(VentanaSec5, text=f"El total cobrado es: ${Total}\n", style="S4.TLabel")
                    texto24.place(relx=0.12, rely=0.5)

                    texto25 = ttk.Label(VentanaSec5, text="------------------------------\n", style="S4.TLabel")
                    texto25.place(relx=0.12, rely=0.56)

                    imagen14 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\bordeArriba.png")
                    subBorde9 = imagen14.subsample(3)
                    BordeDerecho3 = tk.Label(VentanaSec5, bg="#295f48", image=subBorde9)
                    BordeDerecho3.place(relx=0.0, rely=0.0)

                    imagen15 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\bordeAbajo.png")
                    subBorde10 = imagen15.subsample(3)
                    BordeIzquierdo3 = tk.Label(VentanaSec5, bg="#295f48", image=subBorde10)
                    BordeIzquierdo3.place(relx=0.0, rely=0.84)

                    salir = tk.Button(VentanaSec5,
                                    command=ev5,
                                    background="#49ab81",
                                    foreground="#18392b",
                                    activebackground="#dcbb57",
                                    activeforeground="#18392b",
                                    highlightthickness=2,
                                    highlightcolor="#dcbb57",
                                    width=9,
                                    height=1,
                                    border=0,
                                    font=('Arial', 16, 'bold'),
                                    text="Salir",
                                    )
                    salir.place(relx=0.34, rely=0.7)

                def reset_inicio():
                    inicio_var.set("")

                def reset_destino():
                    destino_var.set("")

                def reset_Adulto():
                    Adulto_var.set("")

                VBoletos.withdraw()
                VentanaSec1 = Toplevel()

                VentanaSec1.geometry('1000x720')
                VentanaSec1.configure(bg="#295f48")
                VentanaSec1.title('Compra de boletos')
                VentanaSec1.iconbitmap("C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\IconoVentana.ico")
                VentanaSec1.resizable(width=False, height=False)

                inicio_var = tk.StringVar()
                destino_var = tk.StringVar()
                Adulto_var = tk.StringVar()

                imagen4 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\bordeArriba.png")
                subBorde3 = imagen4.subsample(3)
                BordeDerecho2 = tk.Label(VentanaSec1, bg="#295f48", image=subBorde3)
                BordeDerecho2.place(relx=0.0, rely=0.0)

                imagen5 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\bordeAbajo.png")
                subBorde4 = imagen5.subsample(3)
                BordeIzquierdo2 = tk.Label(VentanaSec1, bg="#295f48", image=subBorde4)
                BordeIzquierdo2.place(relx=0.0, rely=0.86)

                texto1 = ttk.Label(VentanaSec1, text="Elige las opciones de tu viaje!", style="S2.TLabel")
                texto1.place(relx=0.045, rely=0.12)

                salir = tk.Button(VentanaSec1,
                                command=ev2,
                                background="#49ab81",
                                foreground="#18392b",
                                activebackground="#dcbb57",
                                activeforeground="#18392b",
                                highlightthickness=2,
                                highlightcolor="#dcbb57",
                                width=9,
                                height=1,
                                border=0,
                                font=('Arial', 16, 'bold'),
                                text="Salir",
                                )
                salir.place(relx=0.36, rely=0.78)

                Promos1 = tk.Button(VentanaSec1,
                                command=Promos1,
                                background="#49ab81",
                                foreground="#18392b",
                                activebackground="#dcbb57",
                                activeforeground="#18392b",
                                highlightthickness=2,
                                highlightcolor="#dcbb57",
                                width=9,
                                height=1,
                                border=0,
                                font=('Arial', 16, 'bold'),
                                text="Promos",
                                )
                Promos1.place(relx=0.5, rely=0.78)

                CalcMFinal = tk.Button(VentanaSec1,
                                command=MontoFinal,
                                background="#49ab81",
                                foreground="#18392b",
                                activebackground="#dcbb57",
                                activeforeground="#18392b",
                                highlightthickness=2,
                                highlightcolor="#dcbb57",
                                width=14,
                                height=1,
                                border=0,
                                font=('Arial', 16, 'bold'),
                                text="Calcular monto",
                                )
                CalcMFinal.place(relx=0.398, rely=0.62)

                FinalizarCompra = tk.Button(VentanaSec1,
                                command = BoletoComprado,
                                background="#49ab81",
                                foreground="#18392b",
                                activebackground="#dcbb57",
                                activeforeground="#18392b",
                                highlightthickness=2,
                                highlightcolor="#dcbb57",
                                width=14,
                                height=1,
                                border=0,
                                font=('Arial', 16, 'bold'),
                                text="Finalizar compra",
                                )
                FinalizarCompra.place(relx=0.398, rely=0.7)

                Edades = ['5 - 15', '16 - 18', '19 - 29', '30 - 39', '40 - 60+']
                TipoEdades = ttk.Combobox(VentanaSec1,
                                    values=Edades,
                                    background="#49ab81",
                                    foreground="#142b25",
                                    width=11,
                                    height=10,
                                    font=('Fonseca', 25, 'bold'),
                                    justify="center"
                                    )
                TipoEdades.place(relx=0.06, rely=0.3)

                global TipoHorario
                Horario = ['5:00am', '6:20am', '8:40am', '11:00am', '12:20pm', '14:00am', '17:00pm', '20:00pm']
                TipoHorario = ttk.Combobox(VentanaSec1,
                                    values=Horario,
                                    background="#49ab81",
                                    foreground="#142b25",
                                    width=11,
                                    height=10,
                                    font=('Fonseca', 25, 'bold'),
                                    justify="center"
                                    )
                TipoHorario.place(relx=0.347, rely=0.3)

                global TipoCantidad
                Cantidad = ['1', '2', '3', '4', '5', '6']
                TipoCantidad = ttk.Combobox(VentanaSec1,
                                            values=Cantidad,
                                            background="#49ab81",
                                            foreground="#142b25",
                                            width=11,
                                            height=10,
                                            font=('Fonseca', 25, 'bold'),
                                            justify="center"
                                            )
                TipoCantidad.place(relx=0.635, rely=0.3)

                texto2 = ttk.Label(VentanaSec1, text="Edad", style="S1.TLabel")
                texto2.place(relx=0.14, rely=0.22)

                texto3 = ttk.Label(VentanaSec1, text="Horario", style="S1.TLabel")
                texto3.place(relx=0.395, rely=0.22)

                texto4 = ttk.Label(VentanaSec1, text="Cantidad", style="S1.TLabel")
                texto4.place(relx=0.668, rely=0.22)

                texto5 = ttk.Label(VentanaSec1, text="Inicio", style="S1.TLabel")
                texto5.place(relx=0.13, rely=0.46)

                texto6 = ttk.Label(VentanaSec1, text="Destino", style="S1.TLabel")
                texto6.place(relx=0.68, rely=0.46)

                texto7 = ttk.Label(VentanaSec1, text="     Si eres menor a 18, vienes con un adulto?", style="S5.TLabel")
                texto7.place(relx=0.028, rely=0.37)

                Tecate1 = ttk.Radiobutton(VentanaSec1, text="Tecate", variable=inicio_var, value="Tecate", style="S1.TRadiobutton")
                Tecate1.place(relx=0.13, rely=0.55)

                Tijuana1 = ttk.Radiobutton(VentanaSec1, text="Tijuana", variable=inicio_var, value="Tijuana", style="S1.TRadiobutton")
                Tijuana1.place(relx=0.13, rely=0.6)

                Mexicali1 = ttk.Radiobutton(VentanaSec1, text="Mexicali", variable=inicio_var, value="Mexicali", style="S1.TRadiobutton")
                Mexicali1.place(relx=0.13, rely=0.65)

                Ensenada1 = ttk.Radiobutton(VentanaSec1, text="Ensenada", variable=inicio_var, value="Ensenada", style="S1.TRadiobutton")
                Ensenada1.place(relx=0.13, rely=0.7)

                Rosarito1 = ttk.Radiobutton(VentanaSec1, text="Rosarito", variable=inicio_var, value="Rosarito", style="S1.TRadiobutton")
                Rosarito1.place(relx=0.13, rely=0.75)

                Tecate2 = ttk.Radiobutton(VentanaSec1, text="Tecate", variable=destino_var, value="Tecate", style="S1.TRadiobutton")
                Tecate2.place(relx=0.68, rely=0.55)

                Tijuana2 = ttk.Radiobutton(VentanaSec1, text="Tijuana", variable=destino_var, value="Tijuana", style="S1.TRadiobutton")
                Tijuana2.place(relx=0.68, rely=0.6)

                Mexicali2 = ttk.Radiobutton(VentanaSec1, text="Mexicali", variable=destino_var, value="Mexicali", style="S1.TRadiobutton")
                Mexicali2.place(relx=0.68, rely=0.65)

                Ensenada2 = ttk.Radiobutton(VentanaSec1, text="Ensenada", variable=destino_var, value="Ensenada", style="S1.TRadiobutton")
                Ensenada2.place(relx=0.68, rely=0.7)

                Rosarito2 = ttk.Radiobutton(VentanaSec1, text="Rosarito", variable=destino_var, value="Rosarito", style="S1.TRadiobutton")
                Rosarito2.place(relx=0.68, rely=0.75)

                AdultoSi = ttk.Radiobutton(VentanaSec1, text="Si", variable = Adulto_var, value="Si", style="S2.TRadiobutton")
                AdultoSi.place(relx=0.08, rely=0.42)

                AdultoNo = ttk.Radiobutton(VentanaSec1, text="No", variable = Adulto_var, value="No", style="S2.TRadiobutton")
                AdultoNo.place(relx=0.13, rely=0.42)

                resetInicio = tk.Button(VentanaSec1,
                                        command=reset_inicio,
                                        background="#49ab81",
                                        foreground="#18392b",
                                        activebackground="#dcbb57",
                                        activeforeground="#18392b",
                                        highlightthickness=2,
                                        highlightcolor="#dcbb57",
                                        width=9,
                                        height=1,
                                        border=0,
                                        font=('Arial', 16, 'bold'),
                                        text="Reset",
                                        )
                resetInicio.place(relx=0.15, rely=0.82)

                resetDestino = tk.Button(VentanaSec1,
                                        command=reset_destino,
                                        background="#49ab81",
                                        foreground="#18392b",
                                        activebackground="#dcbb57",
                                        activeforeground="#18392b",
                                        highlightthickness=2,
                                        highlightcolor="#dcbb57",
                                        width=9,
                                        height=1,
                                        border=0,
                                        font=('Arial', 16, 'bold'),
                                        text="Reset",
                                        )
                resetDestino.place(relx=0.7, rely=0.82)

                resetAdulto = tk.Button(VentanaSec1,
                                        command=reset_Adulto,
                                        background="#49ab81",
                                        foreground="#18392b",
                                        activebackground="#dcbb57",
                                        activeforeground="#18392b",
                                        highlightthickness=2,
                                        highlightcolor="#dcbb57",
                                        width=7,
                                        height=1,
                                        border=0,
                                        font=('Arial', 16, 'bold'),
                                        text="Reset",
                                        )
                resetAdulto.place(relx=0.2, rely=0.41)

                texto6 = ttk.Label(VentanaSec1, text="$          ", style="S3.TLabel")
                texto6.place(relx=0.41, rely=0.52)

                texto7 = ttk.Label(VentanaSec1, text="Monto", style="S1.TLabel")
                texto7.place(relx=0.412, rely=0.43)

    elif VentanaEleccion == 'Turista':

        global subBorde5, subBorde6, sublogo3

        def ev2():
            VBoletos.deiconify()
            VentanaSec3.destroy()

        
        def MontoEdad2():

            global Mfinal2

            if TipoEdades2.get() == '':
                return None
            
            edad = TipoEdades2.get()

            if edad in ['5 - 15','16 - 18']:
                messagebox.showerror("Error", "No se permiten menores de edad!")
                return None
            
            if TipoClase.get() == '1ra Clase':

                if edad in ['19 - 29', '30 - 39']:
                    Mfinal2 = 1000
                elif edad == '40 - 60+':
                    Mfinal2 = 850
                
            elif TipoClase.get() == '2da Clase':
                if edad in ['19 - 29', '30 - 39']:
                    Mfinal2 = 800
                elif edad == '40 - 60+':
                    Mfinal2 = 700
            
            elif TipoClase.get() == '3ra Clase':
                if edad in ['19 - 29', '30 - 39']:
                    Mfinal2 = 600
                elif edad == '40 - 60+':
                    Mfinal2 = 500


            return True

        def MontoCantidad2():

            global CantidadPersonas2

            try:
                CantidadPersonas2 = int(TipoCantidad2.get())
                return True
            except ValueError:
                messagebox.showerror("Error", "Ingresa un número válido para la cantidad de personas")
                return False

        def MontoFinal2():
            
            if MontoEdad2() is None or MontoCantidad2() is None:
                messagebox.showerror("Error!", "Debes completar los requerimientos")
                return

            def Parte1_2():
                global Mfinal2
                if Mfinal2 is not None and CantidadPersonas2 is not None:
                    if TipoClase.get() == '1ra Clase':
                        if Mfinal2 == 850 and CantidadPersonas2 >= 4:
                            return Mfinal2 * CantidadPersonas2 * (1 - 0.15)
                        elif Mfinal2 == 1000 and CantidadPersonas2 >= 4:
                            return Mfinal2 * CantidadPersonas2 * (1 - 0.15)
                        else:
                            return Mfinal2 * CantidadPersonas2

                    elif TipoClase.get() == '2da Clase':
                        if Mfinal2 == 700 and CantidadPersonas2 >= 4:
                            return Mfinal2 * CantidadPersonas2 * (1 - 0.15)
                        elif Mfinal2 == 800 and CantidadPersonas2 >= 4:
                            return Mfinal2 * CantidadPersonas2 * (1 - 0.15)
                        else:
                            return Mfinal2 * CantidadPersonas2

                    elif TipoClase.get() == '3ra Clase':
                        if Mfinal2 == 500 and CantidadPersonas2 >= 4:
                            return Mfinal2 * CantidadPersonas2 * (1 - 0.15)
                        elif Mfinal2 == 600 and CantidadPersonas2 >= 4:
                            return Mfinal2 * CantidadPersonas2 * (1 - 0.15)
                        else:
                            return Mfinal2 * CantidadPersonas2

                    elif TipoClase.get() == '':
                        messagebox.showerror("Error!", "Debes elegir una clase!")
                        return 0
                else:
                    return 0

            def Parte2_2():
                tarifa2 = 0
                if inicio_var2.get() == "" or destino_var2.get() == "" or inicio_var2.get() == destino_var2.get():
                    messagebox.showerror("Error!", "Elige un inicio y destino válidos!")
                    return 0

                if inicio_var2.get() == "Tecate" and destino_var2.get() == "Tijuana":
                    tarifa2 = 30 
                elif inicio_var2.get() == "Tecate" and destino_var2.get() == "Mexicali":
                    tarifa2 = 40 
                elif inicio_var2.get() == "Tecate" and destino_var2.get() == "Ensenada":
                    tarifa2 = 50 
                elif inicio_var2.get() == "Tecate" and destino_var2.get() == "Rosarito":
                    tarifa2 = 50 

                elif inicio_var2.get() == "Tijuana" and destino_var2.get() == "Tecate":
                    tarifa2 = 30 
                elif inicio_var2.get() == "Tijuana" and destino_var2.get() == "Mexicali":
                    tarifa2 = 40 
                elif inicio_var2.get() == "Tijuana" and destino_var2.get() == "Ensenada":
                    tarifa2 = 50 
                elif inicio_var2.get() == "Tijuana" and destino_var2.get() == "Rosarito":
                    tarifa2 = 50

                elif inicio_var2.get() == "Mexicali" and destino_var2.get() == "Tijuana":
                    tarifa2 = 30 
                elif inicio_var2.get() == "Mexicali" and destino_var2.get() == "Tecate":
                    tarifa2 = 40 
                elif inicio_var2.get() == "Mexicali" and destino_var2.get() == "Ensenada":
                    tarifa2 = 50 
                elif inicio_var2.get() == "Mexicali" and destino_var2.get() == "Rosarito":
                    tarifa2 = 50

                elif inicio_var2.get() == "Ensenada" and destino_var2.get() == "Tijuana":
                    tarifa2 = 50 
                elif inicio_var2.get() == "Ensenada" and destino_var2.get() == "Mexicali":
                    tarifa2 = 50 
                elif inicio_var2.get() == "Ensenada" and destino_var2.get() == "Tecate":
                    tarifa2 = 50 
                elif inicio_var2.get() == "Ensenada" and destino_var2.get() == "Rosarito":
                    tarifa2 = 30 

                elif inicio_var2.get() == "Rosarito" and destino_var2.get() == "Tijuana":
                    tarifa2 = 50 
                elif inicio_var2.get() == "Rosarito" and destino_var2.get() == "Mexicali":
                    tarifa2 = 50 
                elif inicio_var2.get() == "Rosarito" and destino_var2.get() == "Ensenada":
                    tarifa2 = 30 
                elif inicio_var2.get() == "Rosarito" and destino_var2.get() == "Tecate":
                    tarifa2 = 50

                return tarifa2 * CantidadPersonas2

            M3 = Parte1_2()
            M4 = Parte2_2()

            if M3 is None:
                M3 = 0
            if M4 is None:
                M4 = 0

            total2 = M3 + M4
            texto13.config(text="$" + str(total2))

            return total2

        def Promos2():
            global subBorde6, subBorde5

            def ev4():
                VentanaSec3.deiconify()
                VentanaSec4.destroy()

            VentanaSec3.withdraw()
            VentanaSec4 = Toplevel()

            VentanaSec4.geometry('1000x900')
            VentanaSec4.configure(bg = "#295f48")
            VentanaSec4.title('Compra de boletos')
            VentanaSec4.iconbitmap("C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\IconoVentana.ico")
            VentanaSec4.resizable(width = False, height = False)

            texto17 = ttk.Label(VentanaSec4, text="Edades", style="S1.TLabel")
            texto17.place(relx=0.41, rely=0.02)

            texto18 = ttk.Label(VentanaSec4, text="----------------------------------------------------------------\nEn cualquier clase, al elegir tu edad si pasas de los 40\n         años de edad se hace un descuento del 15%\n----------------------------------------------------------------", style="S4.TLabel")
            texto18.place(relx=0.18, rely=0.07)




            texto19 = ttk.Label(VentanaSec4, text="1ra Clase", style="S1.TLabel")
            texto19.place(relx=0.38, rely=0.17)

            texto20 = ttk.Label(VentanaSec4, text="----------------------------------------------------------------------\n  En esta Clase se hara un tour en cada ciudad listada en la\ncompra de boletos, en la compra de esta clase se incluye \n la reservacion de hoteles 5 estrellas con todo incluido en\n     cada ciudad del tour, tambien incluye visitas a lugares\n                    turisticos como playas, jardines, y\n                     lugares iconicos de cada ciudad\n----------------------------------------------------------------------", style="S4.TLabel")
            texto20.place(relx=0.15, rely=0.22)

            texto19 = ttk.Label(VentanaSec4, text="2da Clase", style="S1.TLabel")
            texto19.place(relx=0.38, rely=0.43)

            texto20 = ttk.Label(VentanaSec4, text="----------------------------------------------------------------------\n  En esta Clase se hara un tour en cada ciudad listada en la\ncompra de boletos, en la compra de esta clse se incluye \n la reservacion de hoteles 4 estrellas con todo incluido en\n     cada ciudad del tour, tambien incluye visitas a lugares\n                    turisticos como playas, jardines, y\n                     lugares iconicos de cada ciudad\n----------------------------------------------------------------------", style="S4.TLabel")
            texto20.place(relx=0.15, rely=0.48)

            texto19 = ttk.Label(VentanaSec4, text="3ra Clase", style="S1.TLabel")
            texto19.place(relx=0.38, rely=0.69)

            texto20 = ttk.Label(VentanaSec4, text="----------------------------------------------------------------------\n  En esta Clase se hara un tour en cada ciudad listada en la\n  compra de boletos, en la compra de esta clse se incluye \n    la reservacion de hoteles 2 estrellas (NO tienen todo\n     incluido) en cada ciudad del tour, tambien incluye visitas\n                    a lugares iconicos de cada ciudad\n----------------------------------------------------------------------", style="S4.TLabel")
            texto20.place(relx=0.15, rely=0.74)





            imagen7 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\derecho.png")
            subBorde5 = imagen7.subsample(3)
            BordeDerecho3 = tk.Label(VentanaSec4, bg="#295f48", image=subBorde5)
            BordeDerecho3.place(relx=0.0, rely=0.0)

            imagen8 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\izquierdo.png")
            subBorde6 = imagen8.subsample(3)
            BordeIzquierdo3 = tk.Label(VentanaSec4, bg="#295f48", image=subBorde6)
            BordeIzquierdo3.place(relx=0.91, rely=0.0)

            salir = tk.Button(VentanaSec4,
                            command=ev4,
                            background="#49ab81",
                            foreground="#18392b",
                            activebackground="#dcbb57",
                            activeforeground="#18392b",
                            highlightthickness=2,
                            highlightcolor="#dcbb57",
                            width=9,
                            height=1,
                            border=0,
                            font=('Arial', 16, 'bold'),
                            text="Salir",
                            )
            salir.place(relx=0.4, rely=0.93)

        if TipoBoleto.get() != "":

            if TipoBoleto.get() == "Turista":

                def BoletoComprado2():
                    global subBorde9, subBorde10

                    def ev5():
                        VentanaSec3.deiconify()
                        VentanaSec5.destroy()

                    CantidadBoletos2 = TipoCantidad2.get()
                    InicioViaje2 = inicio_var2.get()
                    DestinoViaje2 = destino_var2.get()
                    HorarioViaje2 = TipoHorario2.get()
                    Total2 = MontoFinal2()
                    Clase = TipoClase.get()
                    

                    VentanaSec3.withdraw()
                    VentanaSec5 = Toplevel()

                    VentanaSec5.geometry('400x600')
                    VentanaSec5.configure(bg="#295f48")
                    VentanaSec5.title('Recibo de Compra')
                    VentanaSec5.iconbitmap("C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\IconoVentana.ico")
                    VentanaSec5.resizable(width=False, height=False)

                    texto19 = ttk.Label(VentanaSec5, text="Recibo", style="S1.TLabel")
                    texto19.place(relx=0.3, rely=0.15)

                    texto20 = ttk.Label(VentanaSec5, text=f"------------------------------\nCantidad de boletos: {CantidadBoletos2}\n", style="S4.TLabel")
                    texto20.place(relx=0.12, rely=0.23)

                    texto21 = ttk.Label(VentanaSec5, text=f"El viaje inicia en: {InicioViaje2}\n", style="S4.TLabel")
                    texto21.place(relx=0.12, rely=0.32)

                    texto22 = ttk.Label(VentanaSec5, text=f"El viaje termina en: {DestinoViaje2}\n", style="S4.TLabel")
                    texto22.place(relx=0.12, rely=0.38)

                    texto23 = ttk.Label(VentanaSec5, text=f"El Viaje inicia a las: {HorarioViaje2}\n", style="S4.TLabel")
                    texto23.place(relx=0.12, rely=0.44)

                    texto24 = ttk.Label(VentanaSec5, text=f"El total cobrado es: ${Total2}\n", style="S4.TLabel")
                    texto24.place(relx=0.12, rely=0.5)

                    texto24 = ttk.Label(VentanaSec5, text=f"El viaje sera en: {Clase}\n", style="S4.TLabel")
                    texto24.place(relx=0.12, rely=0.56)

                    texto25 = ttk.Label(VentanaSec5, text="------------------------------\n", style="S4.TLabel")
                    texto25.place(relx=0.12, rely=0.6)

                    imagen14 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\bordeArriba.png")
                    subBorde9 = imagen14.subsample(3)
                    BordeDerecho3 = tk.Label(VentanaSec5, bg="#295f48", image=subBorde9)
                    BordeDerecho3.place(relx=0.0, rely=0.0)

                    imagen15 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\bordeAbajo.png")
                    subBorde10 = imagen15.subsample(3)
                    BordeIzquierdo3 = tk.Label(VentanaSec5, bg="#295f48", image=subBorde10)
                    BordeIzquierdo3.place(relx=0.0, rely=0.84)

                    salir = tk.Button(VentanaSec5,
                                    command=ev5,
                                    background="#49ab81",
                                    foreground="#18392b",
                                    activebackground="#dcbb57",
                                    activeforeground="#18392b",
                                    highlightthickness=2,
                                    highlightcolor="#dcbb57",
                                    width=9,
                                    height=1,
                                    border=0,
                                    font=('Arial', 16, 'bold'),
                                    text="Salir",
                                    )
                    salir.place(relx=0.34, rely=0.7)

                def reset_inicio2():
                    inicio_var2.set("")

                def reset_destino2():
                    destino_var2.set("")

                VBoletos.withdraw()
                VentanaSec3 = Toplevel()

                VentanaSec3.geometry('1000x720')
                VentanaSec3.configure(bg="#295f48")
                VentanaSec3.title('Compra de boletos')
                VentanaSec3.iconbitmap("C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\IconoVentana.ico")
                VentanaSec3.resizable(width=False, height=False)

                inicio_var2 = tk.StringVar()
                destino_var2 = tk.StringVar()

                imagen4 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\bordeArriba.png")
                subBorde3 = imagen4.subsample(3)
                BordeDerecho2 = tk.Label(VentanaSec3, bg="#295f48", image=subBorde3)
                BordeDerecho2.place(relx=0.0, rely=0.0)

                imagen5 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\bordeAbajo.png")
                subBorde4 = imagen5.subsample(3)
                BordeIzquierdo2 = tk.Label(VentanaSec3, bg="#295f48", image=subBorde4)
                BordeIzquierdo2.place(relx=0.0, rely=0.86)

                texto1 = ttk.Label(VentanaSec3, text="Elige las opciones de tu viaje!", style="S2.TLabel")
                texto1.place(relx=0.045, rely=0.12)

                salir = tk.Button(VentanaSec3,
                                command=ev2,
                                background="#49ab81",
                                foreground="#18392b",
                                activebackground="#dcbb57",
                                activeforeground="#18392b",
                                highlightthickness=2,
                                highlightcolor="#dcbb57",
                                width=9,
                                height=1,
                                border=0,
                                font=('Arial', 16, 'bold'),
                                text="Salir",
                                )
                salir.place(relx=0.36, rely=0.82)

                Promos2 = tk.Button(VentanaSec3,
                                command=Promos2,
                                background="#49ab81",
                                foreground="#18392b",
                                activebackground="#dcbb57",
                                activeforeground="#18392b",
                                highlightthickness=2,
                                highlightcolor="#dcbb57",
                                width=9,
                                height=1,
                                border=0,
                                font=('Arial', 16, 'bold'),
                                text="Promos",
                                )
                Promos2.place(relx=0.5, rely=0.82)

                CalcMFinal2 = tk.Button(VentanaSec3,
                                command=MontoFinal2,
                                background="#49ab81",
                                foreground="#18392b",
                                activebackground="#dcbb57",
                                activeforeground="#18392b",
                                highlightthickness=2,
                                highlightcolor="#dcbb57",
                                width=14,
                                height=1,
                                border=0,
                                font=('Arial', 16, 'bold'),
                                text="Calcular monto",
                                )
                CalcMFinal2.place(relx=0.295, rely=0.75)

                FinalizarCompra2 = tk.Button(VentanaSec3,
                                command = BoletoComprado2,
                                background="#49ab81",
                                foreground="#18392b",
                                activebackground="#dcbb57",
                                activeforeground="#18392b",
                                highlightthickness=2,
                                highlightcolor="#dcbb57",
                                width=14,
                                height=1,
                                border=0,
                                font=('Arial', 16, 'bold'),
                                text="Finalizar compra",
                                )
                FinalizarCompra2.place(relx=0.5, rely=0.75)

                Edades2 = ['5 - 15', '16 - 18', '19 - 29', '30 - 39', '40 - 60+']
                TipoEdades2 = ttk.Combobox(VentanaSec3,
                                    values=Edades2,
                                    background="#49ab81",
                                    foreground="#142b25",
                                    width=11,
                                    height=10,
                                    font=('Fonseca', 25, 'bold'),
                                    justify="center"
                                    )
                TipoEdades2.place(relx=0.06, rely=0.3)

                global TipoHorario2
                Horario2 = ['5:00am', '6:20am', '8:40am', '11:00am', '12:20pm', '14:00am', '17:00pm', '20:00pm']
                TipoHorario2 = ttk.Combobox(VentanaSec3,
                                    values=Horario2,
                                    background="#49ab81",
                                    foreground="#142b25",
                                    width=11,
                                    height=10,
                                    font=('Fonseca', 25, 'bold'),
                                    justify="center"
                                    )
                TipoHorario2.place(relx=0.347, rely=0.3)

                global TipoClase
                clase = ['1ra Clase', '2da Clase', '3ra Clase']
                TipoClase = ttk.Combobox(VentanaSec3,
                                    values=clase,
                                    background="#49ab81",
                                    foreground="#142b25",
                                    width=11,
                                    height=10,
                                    font=('Fonseca', 25, 'bold'),
                                    justify="center"
                                    )
                TipoClase.place(relx=0.347, rely=0.47)

                global TipoCantidad2
                Cantidad2 = ['1', '2', '3', '4', '5', '6']
                TipoCantidad2 = ttk.Combobox(VentanaSec3,
                                            values=Cantidad2,
                                            background="#49ab81",
                                            foreground="#142b25",
                                            width=11,
                                            height=10,
                                            font=('Fonseca', 25, 'bold'),
                                            justify="center"
                                            )
                TipoCantidad2.place(relx=0.635, rely=0.3)

                texto2 = ttk.Label(VentanaSec3, text="Edad", style="S1.TLabel")
                texto2.place(relx=0.14, rely=0.22)

                texto3 = ttk.Label(VentanaSec3, text="Horario", style="S1.TLabel")
                texto3.place(relx=0.395, rely=0.22)

                texto4 = ttk.Label(VentanaSec3, text="Cantidad", style="S1.TLabel")
                texto4.place(relx=0.668, rely=0.22)

                texto5 = ttk.Label(VentanaSec3, text="Inicio", style="S1.TLabel")
                texto5.place(relx=0.08, rely=0.46)

                texto6 = ttk.Label(VentanaSec3, text="Destino", style="S1.TLabel")
                texto6.place(relx=0.73, rely=0.46)

                texto3 = ttk.Label(VentanaSec3, text="Clase", style="S1.TLabel")
                texto3.place(relx=0.427, rely=0.39)
                
                Tecate1 = ttk.Radiobutton(VentanaSec3, text="Tecate", variable=inicio_var2, value="Tecate", style="S1.TRadiobutton")
                Tecate1.place(relx=0.08, rely=0.55)

                Tijuana1 = ttk.Radiobutton(VentanaSec3, text="Tijuana", variable=inicio_var2, value="Tijuana", style="S1.TRadiobutton")
                Tijuana1.place(relx=0.08, rely=0.6)

                Mexicali1 = ttk.Radiobutton(VentanaSec3, text="Mexicali", variable=inicio_var2, value="Mexicali", style="S1.TRadiobutton")
                Mexicali1.place(relx=0.08, rely=0.65)

                Ensenada1 = ttk.Radiobutton(VentanaSec3, text="Ensenada", variable=inicio_var2, value="Ensenada", style="S1.TRadiobutton")
                Ensenada1.place(relx=0.08, rely=0.7)

                Rosarito1 = ttk.Radiobutton(VentanaSec3, text="Rosarito", variable=inicio_var2, value="Rosarito", style="S1.TRadiobutton")
                Rosarito1.place(relx=0.08, rely=0.75)

                Tecate2 = ttk.Radiobutton(VentanaSec3, text="Tecate", variable=destino_var2, value="Tecate", style="S1.TRadiobutton")
                Tecate2.place(relx=0.73, rely=0.55)

                Tijuana2 = ttk.Radiobutton(VentanaSec3, text="Tijuana", variable=destino_var2, value="Tijuana", style="S1.TRadiobutton")
                Tijuana2.place(relx=0.73, rely=0.6)

                Mexicali2 = ttk.Radiobutton(VentanaSec3, text="Mexicali", variable=destino_var2, value="Mexicali", style="S1.TRadiobutton")
                Mexicali2.place(relx=0.73, rely=0.65)

                Ensenada2 = ttk.Radiobutton(VentanaSec3, text="Ensenada", variable=destino_var2, value="Ensenada", style="S1.TRadiobutton")
                Ensenada2.place(relx=0.73, rely=0.7)

                Rosarito2 = ttk.Radiobutton(VentanaSec3, text="Rosarito", variable=destino_var2, value="Rosarito", style="S1.TRadiobutton")
                Rosarito2.place(relx=0.73, rely=0.75)

                resetInicio2 = tk.Button(VentanaSec3,
                                        command=reset_inicio2,
                                        background="#49ab81",
                                        foreground="#18392b",
                                        activebackground="#dcbb57",
                                        activeforeground="#18392b",
                                        highlightthickness=2,
                                        highlightcolor="#dcbb57",
                                        width=9,
                                        height=1,
                                        border=0,
                                        font=('Arial', 16, 'bold'),
                                        text="Reset",
                                        )
                resetInicio2.place(relx=0.1, rely=0.82)

                resetDestino2 = tk.Button(VentanaSec3,
                                        command=reset_destino2,
                                        background="#49ab81",
                                        foreground="#18392b",
                                        activebackground="#dcbb57",
                                        activeforeground="#18392b",
                                        highlightthickness=2,
                                        highlightcolor="#dcbb57",
                                        width=9,
                                        height=1,
                                        border=0,
                                        font=('Arial', 16, 'bold'),
                                        text="Reset",
                                        )
                resetDestino2.place(relx=0.75, rely=0.82)

                texto13 = ttk.Label(VentanaSec3, text="$          ", style="S3.TLabel")
                texto13.place(relx=0.41, rely=0.65)

                texto14 = ttk.Label(VentanaSec3, text="Monto", style="S1.TLabel")
                texto14.place(relx=0.412, rely=0.57)

    else:
        messagebox.showerror("Error!", "Elige el tipo de boleto!")

VBoletos = tk.Tk()

estilo = ttk.Style()
estilo.configure("S1.TLabel",
                font=('Fonseca', 30, 'bold'),
                background="#295f48",
                foreground="#142b25"
                )

estilo.configure("S2.TLabel",
                font=('Fonseca', 40, 'bold'),
                background="#295f48",
                foreground="#142b25"
                )

estilo.configure("S3.TLabel",
                font=('Fonseca', 30, 'bold'),
                background="#eeeeee",
                foreground="#142b25"
                )

estilo.configure("S4.TLabel",
                font=('Fonseca', 15, 'bold'),
                background="#295f48",
                foreground="#142b25"
                )

estilo.configure("S5.TLabel",
                font=('Fonseca', 10, 'bold'),
                background="#295f48",
                foreground="#142b25"
                )

estilo.configure("S1.TRadiobutton",
                font=('Fonseca', 20, 'bold'),
                background="#295f48",
                foreground="#142b25",
                indicatorcolor="#dcbb57",
                indicatormargin=10
                )

estilo.configure("S2.TRadiobutton",
                font=('Fonseca', 15, 'bold'),
                background="#295f48",
                foreground="#142b25",
                indicatorcolor="#dcbb57",
                indicatormargin=10
                )

VBoletos.geometry("600x700")
VBoletos.title("Venta de boletos de tren")
VBoletos.configure(bg="#295f48")
VBoletos.resizable(width=False, height=False)
VBoletos.iconbitmap("C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\IconoVentana.ico")

imagen1 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\trenlogo.png")
sublogo1 = imagen1.subsample(2)
logo1 = tk.Label(VBoletos, bg="#295f48", image=sublogo1)
logo1.place(relx=0.35, rely=0.03)

imagen2 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\derecho.png")
subBorde1 = imagen2.subsample(3)
BordeDerecho1 = tk.Label(VBoletos, bg="#295f48", image=subBorde1)
BordeDerecho1.place(relx=0.0, rely=0.0)

imagen3 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\izquierdo.png")
subBorde2 = imagen3.subsample(3)
BordeIzquierdo1 = tk.Label(VBoletos, bg="#295f48", image=subBorde2)
BordeIzquierdo1.place(relx=0.855, rely=0.0)

texto1 = ttk.Label(VBoletos, text="Elige una opcion", style="S1.TLabel")
texto1.place(relx=0.18, rely=0.58)

Tipos = ['Viaje', 'Turista']
TipoBoleto = ttk.Combobox(VBoletos,
                        values=Tipos,
                        background="#49ab81",
                        foreground="#142b25",
                        width=11,
                        height=10,
                        font=('Fonseca', 25, 'bold'),
                        justify="center"
                        )
TipoBoleto.place(relx=0.282, rely=0.66)

comprar = tk.Button(VBoletos, text="comprar",
                    command=VentaBoletos,
                    background="#49ab81",
                    foreground="#142b25",
                    activebackground="#dcbb57",
                    activeforeground="#18392b",
                    highlightthickness=2,
                    highlightcolor="#dcbb57",
                    width=18,
                    height=2,
                    border=0,
                    font=('Fonseca', 16, 'bold')
                    )
comprar.place(relx=0.295, rely=0.76)

salir = tk.Button(VBoletos, text="salir",
                command=salir,
                background="#49ab81",
                foreground="#142b25",
                activebackground="#dcbb57",
                activeforeground="#18392b",
                highlightthickness=2,
                highlightcolor="#dcbb57",
                width=18,
                height=2,
                border=0,
                font=('Fonseca', 16, 'bold')
                )
salir.place(relx=0.295, rely=0.88)

VBoletos.mainloop()

#falta terminar seccion turista