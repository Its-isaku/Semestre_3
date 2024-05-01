#Librerias
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


#funciones
def Login(username, password):
    Usuario_correcto = "Isai"
    Password_correcto = "IsaiUabc2024"

    if not username.get() or not password.get():
        messagebox.showwarning("Cuidado!", "Se requieren ambos datos")
    elif username.get() == Usuario_correcto and password.get() == Password_correcto:
        Ventana_nueva = Toplevel(login)
        Ventana_nueva.title("Ventana Nueva!")
        Label(Ventana_nueva, text="Cool", font=('Comfortaa', 30)).pack()
    else:
        messagebox.showerror("Error", "username o password incorrectos")

def exit():
    login.destroy()

# Creaando ventana
login = Tk()

# parameters de ventana
login.geometry("600x600")
login.title("Login")
login.configure(bg="#071b40")

# icono de ventana
icon_img = Image.open('C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\Tareas\\M3_3\\imagen.png')
tk_icon_img = ImageTk.PhotoImage(icon_img)
login.iconphoto(False, tk_icon_img)

# Creando labels , widgets y botones
Label(login, text="Login", font=('Comfortaa', 80), bg="#071b40", fg="#e0e2d0").place(relx=0.30, rely=0.05)
Label(login, text="Username", font=('Comfortaa', 30), bg="#071b40", fg="#e0e2d0").place(relx=0.05, rely=0.50)
Label(login, text="Password", font=('Comfortaa', 30), bg="#071b40", fg="#e0e2d0").place(relx=0.05, rely=0.64)

user_entry = Entry(login, width=30, justify=CENTER, font=('Comfortaa', 15))
user_entry.place(relx=0.40, rely=0.52)

pass_entry = Entry(login, show="*", width=30, justify=CENTER, font=('Comfortaa', 15))
pass_entry.place(relx=0.40, rely=0.66)

Button(login, text="Login", width=15, height=2, command=lambda: Login(user_entry, pass_entry), bg="#e0e2d0", fg="#1b1c1e").place(relx=0.145, rely=0.8)
salir = Button(text='Salir',width=15, height=2, command=exit, bg = "tomato", fg = "white").place(relx=.745, rely=0.8)


# Cargando segunda imagen
img_path = "C:\\Users\\RogSt\\Desktop\\Coding\\ProgEst\\Tareas\\M3_3\\imagen2.png"
original_img2 = Image.open(img_path)
tamaño_img2 = original_img2.resize((120, 120), Image.LANCZOS)
tk_img2 = ImageTk.PhotoImage(tamaño_img2)
logo_label = Label(login, image=tk_img2, bg="#071b40")
logo_label.place(relx=0.43, rely=0.28)
logo_label.image = tk_img2 

# cerrar la ventana
login.mainloop()
