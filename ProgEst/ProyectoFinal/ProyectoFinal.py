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
            if TipoEdades.get() == '5 - 15':
                Mfinal = 40
            elif TipoEdades.get() in ['16 - 18', '19 - 29', '30 - 39']:
                Mfinal = 70 
            elif TipoEdades.get() == '40 - 60+':
                Mfinal = 45
            else:
                messagebox.showerror("Error", "Seleccione una edad válida")

        def MontoCantidad():
            global CantidadPersonas
            try:
                CantidadPersonas = int(TipoCantidad.get())
            except ValueError:
                messagebox.showerror("Error", "Seleccione una cantidad válida")

        def MontoFinal():
            MontoEdad()
            MontoCantidad()

            def Parte1():
                if Mfinal == 45 and CantidadPersonas >= 4:
                    return Mfinal * CantidadPersonas * (1 - 0.15)
                elif Mfinal == 70 and CantidadPersonas >= 4:
                    return Mfinal * CantidadPersonas * (1 - 0.15)
                elif Mfinal == 40 and CantidadPersonas >= 4:
                    return Mfinal * CantidadPersonas * (1 - 0.15)
                elif Mfinal == 40 and CantidadPersonas <= 3:
                    return Mfinal * CantidadPersonas
                elif Mfinal == 70 and CantidadPersonas <= 3:
                    return Mfinal * CantidadPersonas
                elif Mfinal == 45 and CantidadPersonas <= 3:
                    return Mfinal * CantidadPersonas

            def Parte2():
                tarifa = 0
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

            texto8 = ttk.Label(VentanaSec2, text="sistema de cobro:", style="S1.TLabel")
            texto8.place(relx=0.23, rely=0.05)

            texto9 = ttk.Label(VentanaSec2, text="-----------------------------------------------------\n Para saber el monto total que se cobrara, \n primero se calcula cuanto se cobra cada\n boleto dependiendo de la edad del individuo\n despues se suma el costo de cada boleto y\n se obtiene el valor total que sera cobrado\n-----------------------------------------------------", style="S4.TLabel")
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
                def reset_inicio():
                    inicio_var.set("")

                def reset_destino():
                    destino_var.set("")

                VBoletos.withdraw()
                VentanaSec1 = Toplevel()

                VentanaSec1.geometry('1000x720')
                VentanaSec1.configure(bg="#295f48")
                VentanaSec1.title('Compra de boletos')
                VentanaSec1.iconbitmap("C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\IconoVentana.ico")
                VentanaSec1.resizable(width=False, height=False)

                inicio_var = tk.StringVar()
                destino_var = tk.StringVar()

                imagen4 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\bordeArriba.png")
                subBorde3 = imagen4.subsample(3)
                BordeDerecho2 = tk.Label(VentanaSec1, bg="#295f48", image=subBorde3)
                BordeDerecho2.place(relx=0.0, rely=0.0)

                imagen5 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\bordeAbajo.png")
                subBorde4 = imagen5.subsample(3)
                BordeIzquierdo2 = tk.Label(VentanaSec1, bg="#295f48", image=subBorde4)
                BordeIzquierdo2.place(relx=0.0, rely=0.86)

                imagen6 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\trenlogo2.png")
                sublogo2 = imagen6.subsample(3)
                logot2 = tk.Label(VentanaSec1, bg="#295f48", image=sublogo2)
                logot2.place(relx=0.43, rely=0.22)

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
                salir.place(relx=0.43, rely=0.78)

                Promos1 = tk.Button(VentanaSec1,
                                command=Promos1,
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
                                text="Promos",
                                )
                Promos1.place(relx=0.398, rely=0.7)

                Comprar = tk.Button(VentanaSec1,
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
                                text="Comprar",
                                )
                Comprar.place(relx=0.398, rely=0.62)

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

                texto3 = ttk.Label(VentanaSec1, text="Cantidad", style="S1.TLabel")
                texto3.place(relx=0.668, rely=0.22)

                texto4 = ttk.Label(VentanaSec1, text="Inicio", style="S1.TLabel")
                texto4.place(relx=0.13, rely=0.46)

                texto5 = ttk.Label(VentanaSec1, text="Destino", style="S1.TLabel")
                texto5.place(relx=0.68, rely=0.46)

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

                texto6 = ttk.Label(VentanaSec1, text="$          ", style="S3.TLabel")
                texto6.place(relx=0.41, rely=0.52)

                texto7 = ttk.Label(VentanaSec1, text="Monto", style="S1.TLabel")
                texto7.place(relx=0.412, rely=0.43)

    elif VentanaEleccion == 'Turista':

        global subBorde5, subBorde6, sublogo3

        def ev3():
            VBoletos.deiconify()
            VentanaSec3.destroy()

        def MontoEdad2():
            global Mfinal2
            if TipoEdades2.get() == '5 - 15':
                Mfina2 = 40
            elif TipoEdades2.get() in ['16 - 18', '19 - 29', '30 - 39']:
                Mfinal2 = 70 
            elif TipoEdades2.get() == '40 - 60+':
                Mfinal2 = 45
            else:
                messagebox.showerror("Error", "Seleccione una edad válida")

        def MontoCantidad2():
            global CantidadPersonas2
            try:
                CantidadPersonas2 = int(TipoCantidad2.get())
            except ValueError:
                messagebox.showerror("Error", "Seleccione una cantidad válida")

        def MontoFinal2():
            MontoEdad2()
            MontoCantidad2()

            def Parte1_2():
                if Mfinal2 == 45 and CantidadPersonas2 >= 4:
                    return Mfinal2 * CantidadPersonas2 * (1 - 0.15)
                elif Mfinal2 == 70 and CantidadPersonas2 >= 4:
                    return Mfinal2 * CantidadPersonas2 * (1 - 0.15)
                elif Mfinal2 == 40 and CantidadPersonas2 >= 4:
                    return Mfinal2 * CantidadPersonas2 * (1 - 0.15)
                elif Mfinal2 == 40 and CantidadPersonas2 <= 3:
                    return Mfinal2 * CantidadPersonas2
                elif Mfinal2 == 70 and CantidadPersonas2 <= 3:
                    return Mfinal2 * CantidadPersonas2
                elif Mfinal2 == 45 and CantidadPersonas2 <= 3:
                    return Mfinal2 * CantidadPersonas2

            def Parte2_2():
                tarifa2 = 0
                if inicio_var2.get() == "Tecate" and destino_var2.get() == "Tijuana":
                    tarifa2 = 30 
                elif inicio_var2.get() == "Tecate" and destino_var2.get() == "Mexicali":
                    tarifa2 = 40 
                elif inicio_var2.get() == "Tecate" and destino_var2.get() == "Ensenada":
                    tarifa2 = 50 
                elif inicio_var2.get() == "Tecate" and destino_var2.get() == "Rosarito":
                    tarif2a = 50 

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

            total2 = M3 + M4
            texto13.config(text="$" + str(total2))

        def Promos2():
            global subBorde7, subBorde8

            def ev4():
                VentanaSec3.deiconify()
                VentanaSec4.destroy()

            VentanaSec3.withdraw()
            VentanaSec4 = Toplevel()

            VentanaSec4.geometry('800x600')
            VentanaSec4.configure(bg="#295f48")
            VentanaSec4.title('Compra de boletos')
            VentanaSec4.iconbitmap("C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\IconoVentana.ico")
            VentanaSec4.resizable(width=False, height=False)

            texto15 = ttk.Label(VentanaSec4, text="sistema de cobro:", style="S1.TLabel")
            texto15.place(relx=0.23, rely=0.05)

            texto16 = ttk.Label(VentanaSec4, text="-----------------------------------------------------\n Para saber el monto total que se cobrara, \n primero se calcula cuanto se cobra cada\n boleto dependiendo de la edad del individuo\n despues se suma el costo de cada boleto y\n se obtiene el valor total que sera cobrado\n-----------------------------------------------------", style="S4.TLabel")
            texto16.place(relx=0.15, rely=0.15)

            texto17 = ttk.Label(VentanaSec4, text="Edades", style="S1.TLabel")
            texto17.place(relx=0.38, rely=0.5)

            texto18 = ttk.Label(VentanaSec4, text="------------------------\n De la edad 40 hacia\n adelante se hace un\n descuento del 15%\n------------------------", style="S4.TLabel")
            texto18.place(relx=0.33, rely=0.6)

            imagen12 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\derecho.png")
            subBorde7 = imagen12.subsample(3)
            BordeDerecho5 = tk.Label(VentanaSec4, bg="#295f48", image=subBorde7)
            BordeDerecho5.place(relx=0.0, rely=0.0)

            imagen13 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\izquierdo.png")
            subBorde8 = imagen13.subsample(3)
            BordeIzquierdo5 = tk.Label(VentanaSec4, bg="#295f48", image=subBorde8)
            BordeIzquierdo5.place(relx=0.89, rely=0.0)

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
            salir.place(relx=0.4, rely=0.9)

        if TipoBoleto.get() != "":
            if TipoBoleto.get() == "Turista":
                def reset_inicio2():
                    inicio_var2.set("")

                def reset_destino2():
                    destino_var.set("")

                VBoletos.withdraw()
                VentanaSec3 = Toplevel()

                VentanaSec3.geometry('1000x720')
                VentanaSec3.configure(bg="#295f48")
                VentanaSec3.title('Compra de boletos')
                VentanaSec3.iconbitmap("C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\IconoVentana.ico")
                VentanaSec3.resizable(width=False, height=False)

                inicio_var2 = tk.StringVar()
                destino_var2 = tk.StringVar()

                imagen9 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\bordeArriba.png")
                subBorde5 = imagen9.subsample(3)
                BordeDerecho4 = tk.Label(VentanaSec3, bg="#295f48", image=subBorde5)
                BordeDerecho4.place(relx=0.0, rely=0.0)

                imagen10 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\bordeAbajo.png")
                subBorde6 = imagen10.subsample(3)
                BordeIzquierdo4 = tk.Label(VentanaSec3, bg="#295f48", image=subBorde6)
                BordeIzquierdo4.place(relx=0.0, rely=0.86)

                imagen11 = tk.PhotoImage(file="C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\ProyectoFinal\\imagenes\\trenlogo2.png")
                sublogo3 = imagen11.subsample(3)
                logo3 = tk.Label(VentanaSec3, bg="#295f48", image=sublogo3)
                logo3.place(relx=0.43, rely=0.22)

                texto8 = ttk.Label(VentanaSec3, text="Elige las opciones de tu viaje!", style="S2.TLabel")
                texto8.place(relx=0.045, rely=0.12)

                salir2 = tk.Button(VentanaSec3,
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
                salir2.place(relx=0.43, rely=0.78)

                Promos2 = tk.Button(VentanaSec3,
                                    command=Promos2,
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
                                    text="Promos",
                                    )
                Promos2.place(relx=0.398, rely=0.7)

                Comprar2 = tk.Button(VentanaSec3,
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
                                    text="Comprar",
                                    )
                Comprar2.place(relx=0.398, rely=0.62)

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

                texto9 = ttk.Label(VentanaSec3, text="Edad", style="S1.TLabel")
                texto9.place(relx=0.14, rely=0.22)

                texto10 = ttk.Label(VentanaSec3, text="Cantidad", style="S1.TLabel")
                texto10.place(relx=0.668, rely=0.22)

                texto11 = ttk.Label(VentanaSec3, text="Inicio", style="S1.TLabel")
                texto11.place(relx=0.13, rely=0.46)

                texto12 = ttk.Label(VentanaSec3, text="Destino", style="S1.TLabel")
                texto12.place(relx=0.68, rely=0.46)

                Tecate3 = ttk.Radiobutton(VentanaSec3, text="Tecate", variable=inicio_var2, value="Tecate", style="S1.TRadiobutton")
                Tecate3.place(relx=0.13, rely=0.55)

                Tijuana3 = ttk.Radiobutton(VentanaSec3, text="Tijuana", variable=inicio_var2, value="Tijuana", style="S1.TRadiobutton")
                Tijuana3.place(relx=0.13, rely=0.6)

                Mexicali3 = ttk.Radiobutton(VentanaSec3, text="Mexicali", variable=inicio_var2, value="Mexicali", style="S1.TRadiobutton")
                Mexicali3.place(relx=0.13, rely=0.65)

                Ensenada3 = ttk.Radiobutton(VentanaSec3, text="Ensenada", variable=inicio_var2, value="Ensenada", style="S1.TRadiobutton")
                Ensenada3.place(relx=0.13, rely=0.7)

                Rosarito3 = ttk.Radiobutton(VentanaSec3, text="Rosarito", variable=inicio_var2, value="Rosarito", style="S1.TRadiobutton")
                Rosarito3.place(relx=0.13, rely=0.75)

                Tecate4 = ttk.Radiobutton(VentanaSec3, text="Tecate", variable=destino_var2, value="Tecate", style="S1.TRadiobutton")
                Tecate4.place(relx=0.68, rely=0.55)

                Tijuana4 = ttk.Radiobutton(VentanaSec3, text="Tijuana", variable=destino_var2, value="Tijuana", style="S1.TRadiobutton")
                Tijuana4.place(relx=0.68, rely=0.6)

                Mexicali4 = ttk.Radiobutton(VentanaSec3, text="Mexicali", variable=destino_var2, value="Mexicali", style="S1.TRadiobutton")
                Mexicali4.place(relx=0.68, rely=0.65)

                Ensenada4 = ttk.Radiobutton(VentanaSec3, text="Ensenada", variable=destino_var2, value="Ensenada", style="S1.TRadiobutton")
                Ensenada4.place(relx=0.68, rely=0.7)

                Rosarito4 = ttk.Radiobutton(VentanaSec3, text="Rosarito", variable=destino_var2, value="Rosarito", style="S1.TRadiobutton")
                Rosarito4.place(relx=0.68, rely=0.75)

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
                resetInicio2.place(relx=0.15, rely=0.82)

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
                resetDestino2.place(relx=0.7, rely=0.82)

                texto13 = ttk.Label(VentanaSec3, text="$          ", style="S3.TLabel")
                texto13.place(relx=0.41, rely=0.52)

                texto14 = ttk.Label(VentanaSec3, text="Monto", style="S1.TLabel")
                texto14.place(relx=0.412, rely=0.43)
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

estilo.configure("S1.TRadiobutton",
                font=('Fonseca', 20, 'bold'),
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




""" 
Faltante:

    -> viajes <-
    -Restrinccion para que menores de edad no viajen sin adultos
    -agregar horarios
    -Messagebox que tenga los datos finales(costos, cantidad de boletos, horario, inicio y destino de viaje)

    -> turistas <-
    -Restrinccion para que menores de edad no viajen sin adultos
    -agregar horarios
    -Messagebox que tenga los datos finales(costos, cantidad de boletos, horario, inicio y destino de viaje)
    -agregar combobox para elegir la clase del viaje

"""