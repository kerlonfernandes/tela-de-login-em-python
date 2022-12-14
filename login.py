from tkinter import *
import tkinter.messagebox as MessageBox
from PIL import Image, ImageTk

login = Tk()
login.geometry("800x500+565+270")
login.title("Sistema de Login")

texto_login = Label(login, text="Entre com o Login", font=("Arial Black", 17), fg="#3b3b3b")
texto_login.place(x=25, y=50)

#usuario

img_usuario = Image.open("Imagem/username.png")
img_usuario = img_usuario.resize((35,35))
img_usuario = ImageTk.PhotoImage(img_usuario)

label_img_usuario = Label (login, image=img_usuario, compound=LEFT, font=('Ivy 10 bold'), anchor='nw')
label_img_usuario.place(x=240, y=145)

#senha 
img_senha = Image.open("Imagem/senha.png")
img_senha = img_senha.resize((35,35))
img_senha = ImageTk.PhotoImage(img_senha)

label_img_senha = Label (login, image=img_senha, compound=LEFT, font=('Ivy 10 bold'), anchor='nw')
label_img_senha.place(x=240, y=215)

#campos de usuario
campo_usuario = Entry(login, text="", font=(10), width=20)
campo_usuario.place(x=317, y=150)

#campo Senha
campo_senha = Entry(login, text="", font=(10), width=20, show="*")
campo_senha.place(x=317, y=220)


#botao
botao_entrar  = Button(login, text="Entrar No Sistema", bg="#3b3b3b", fg="white", font=("Arial Black",11))
botao_entrar.place(x=310, y=330)

login.mainloop()