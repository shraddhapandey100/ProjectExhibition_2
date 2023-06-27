from tkinter import *
from tkinter.ttk import Progressbar
import time
import denGuardEngine
from PIL import Image, ImageTk

root_neuron = Tk()

# Geometry
root_neuron.geometry("1000x600+150+120")
root_neuron.minsize(1000, 600)
root_neuron.maxsize(1000, 600)
root_neuron.title("DenGuard Antivirus")

image = Image.open("D:\\pythonProject\\DenGuard\\AntiviursProject\\Logo.jpg")
resize_image = image.resize((950, 600))
photo = ImageTk.PhotoImage(image)
img = ImageTk.PhotoImage(resize_image)

label2 = Label(image=img)
label2.pack()

label = Label(root_neuron, text="DenGuard", relief="solid", fg="black", bg="cyan", font=("arial", 30, "bold"))
label.place(x=390, y=75)

pb = Progressbar(
    root_neuron,
    orient=HORIZONTAL,
    length=100,
    mode='determinate'
)
pb.place(x=70, y=300)

txt = Label(
    root_neuron,
    text='0%',
    bg='#345',
    fg='#fff'
)
txt.place(x=175, y=300)

def step():
    for i in range(5):
        root_neuron.update_idletasks()
        pb['value'] += 20
        time.sleep(0.5)
        txt['text'] = str(pb['value']) + '%'
    k = 1
    while k > 0:
        denGuardEngine.virusScanner("D:\\pythonProject\\DenGuard\\AntiviursProject")
        denGuardEngine.virusRemover()
        denGuardEngine.ramBooster()
        denGuardEngine.junkFileRemover()
        k = k - 1

Button(
    root_neuron,
    text='Start',
    command=step
).place(x=100, y=330)

def exit1():
    exit()

button = Button(root_neuron, text="virusScanner", relief="solid", fg="white", bg="Green",
                font=("yellow", 16, "bold"),
                command=lambda: denGuardEngine.virusScanner("D:\\pythonProject\\DenGuard\\AntiviursProject"))
button.place(x=60, y=515)

button = Button(root_neuron, text="virusRemover", relief="solid", fg="white", bg="red",
                font=("arial", 16, "bold"),
                command=denGuardEngine.virusRemover)
button.place(x=260, y=515)

button = Button(root_neuron, text="ramBooster", relief="solid", fg="white", bg="Green",
                font=("arial", 16, "bold"),
                command=denGuardEngine.ramBooster)
button.place(x=450, y=515)

button = Button(root_neuron, text="junkFileRemover", relief="solid", fg="white", bg="Green",
                font=("arial", 16, "bold"),
                command=denGuardEngine.junkFileRemover)
button.place(x=625, y=515)

button = Button(root_neuron, text="Quit", relief="solid", fg="white", bg="Green", font=("arial", 16, "bold"),
                command=exit1)
button.place(x=835, y=515)

root_neuron.mainloop()
