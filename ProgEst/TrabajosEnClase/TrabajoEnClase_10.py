import tkinter as tk

login = tk.Tk()


login.geometry('1200x800')
login.title('Login')
login.config(bg = "black")
login.config(cursor = "dot" )
login.resizable(width= True, height= True)

lbl = tk.Label(login, text = "Contraseña: ",fg = "white",bg = "black", font = "Helvetica 20").place(relx = .02, rely =.02)
txt = tk.Entry(login, show = "*", justify = tk.CENTER).place(relx = .03, rely =.08)    
btn = tk.Button(login, text = "Exit", bg = "black", font = "Helvetica 20", width = 10, height = 1, background = "white", command = exit).place(relx = .03, rely = .15)



login.mainloop()