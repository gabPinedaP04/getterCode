from tkinter import *
import subprocess
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog
import pytesseract
from pytesseract import pytesseract
from PIL import Image, ImageTk
import time


import os



root = Tk()
root.title("Título")
root.geometry("800x800")




root.resizable(0,1)


print(pytesseract.get_tesseract_version)


def takeScreenshot():
    minimizeWindow()
    os.system("gnome-screenshot -a -f screenshot.png")

    print("captura tomada")


    while not os.path.exists(file_path):
        time.sleep(0.1)  # Pausa de 100ms para verificar si el archivo ya existe

    # Mostrar la captura si el archivo existe
    if os.path.isfile(file_path):
        show_screenshot(file_path)
        getText(file_path)
        subprocess.Popen(['notify-send','Captura tomada, extrayendo texto...'])
        


    



file_path = 'screenshot.png'


def getText(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    print(text)


def getImage():
    file_path = filedialog.askopenfilename()
    if file_path:
        print(file_path)


        image = Image.open(file_path)

        text = pytesseract.image_to_string(image)
        print(text)


def askChatGPT():
    print("asking gpt4...")




        


buttonUpload = Button(root, text="Subir imagen", command=getImage)


buttonUpload.pack()


buttonScrenshot = Button(root, text="Seleccionar codigo", command=takeScreenshot)

buttonScrenshot.pack()  


buttonChatGpt = Button(root, text="Ask ChatGPT", command=askChatGPT)



buttonChatGpt.pack()


##Mostrar la imagennn --- 

image = Image.open(file_path)
photo = ImageTk.PhotoImage(image)

label = Label(root, image = photo)
label.image = photo
label.pack()


def show_screenshot(file_path):
    # Abrir la imagen
    img = Image.open(file_path)
    
    # Redimensionar la imagen para ajustarla a la ventana si es necesario
    img.thumbnail((400, 400))  # Ajustar el tamaño de la imagen si es necesario
    
    # Convertir la imagen a un formato compatible con Tkinter
    img_tk = ImageTk.PhotoImage(img)

    
    
    # Mostrar la imagen en la ventana
    label.config(image=img_tk)
    label.image = img_tk  # Guardar una referencia de la imagen para evitar que se recoja como basura

    
    

def minimizeWindow():
    root.iconify()
    


###
"""image = Image.open(file_path)
photo = ImageTk.PhotoImage(image)

label = Label(root, image = photo)
label.image = photo
label.grid(row=1, column=1, padx=10, pady=10)"""




## estilos 



style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)




root.mainloop()
