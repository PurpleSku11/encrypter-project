from cryptography.fernet import Fernet
from tkinter import *
from termcolor import cprint , colored
from pyfiglet import figlet_format,Figlet

window = Tk()
window.title('Decrypter')

myLabel = Label(window, text="Decrypter", width=10, height=0)
myLabel.config(font=("ComicSans", 44))
myLabel.pack()

myLabel = Label(window, text="Input Name | (Form <Filename>.txt)")
myLabel.pack()


e = Entry(window, width=50, borderwidth=5)
e.pack()

myLabel = Label(window, text="Output Name | E.g.(filename.txt)")
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

    Dec_File_Name = r.get()

    f = Fernet(Enc_Key)

    with open(File_Name, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open(Dec_File_Name, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


button = Button(window,text='Decrypt the file!')
button.config(command=click)
button.pack()

myLabel = Label(window, text="Purple da haker :)")
myLabel.pack()

window.mainloop()
