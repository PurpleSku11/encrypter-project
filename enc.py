from cryptography.fernet import Fernet
from tkinter import *
from termcolor import cprint , colored
from pyfiglet import figlet_format,Figlet

window = Tk()
window.title('Encrypter')

myLabel = Label(window, text="Encrypter", width=10, height=0)
myLabel.config(font=("ComicSans", 44))
myLabel.pack()

myLabel = Label(window, text="Input Name | (Form <Filename>.txt)")
myLabel.pack()


e = Entry(window, width=50, borderwidth=5)
e.pack()

myLabel = Label(window, text="Output Name | E.g.(filename.enc)")
myLabel.pack()

r = Entry(window, width=50, borderwidth=5)
r.pack()

myLabel = Label(window, text="Encryption Key")
myLabel.pack()

w = Entry(window, width=50, borderwidth=5)
w.pack()

def click():

    File_Name = e.get()

    Enc_Key = w.get()

    Enc_File_Name = r.get()

    f = Fernet(Enc_Key)

    with open(File_Name, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open(Enc_File_Name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def keygen():

    genkey = Fernet.generate_key()

    h.delete(0, 1000)
    h.insert(0, genkey)
    h.pack()




Button1 = Button(window, text='Encrypt the file')
Button1.config(command=click)
Button1.pack()

button2 = Button(window, text='Generate Encryption Key')
button2.config(command=keygen)
button2.pack()

h = Entry(window, width=50, borderwidth=5)

myLabel = Label(window, text="Purple da haker :)")
myLabel.pack()

window.mainloop()
