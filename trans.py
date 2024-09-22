from tkinter import*
from PIL import Image,ImageTk
from googletrans import Translator
import googletrans
from googletrans import Translator 

root = Tk()
root.title('Google Galaxy')
root.geometry('500x630')
root.iconbitmap('logo.ico')

load = Image.open('background.png')
render = ImageTk.PhotoImage(load)
img = Label(root, image = render)
img. place(x = 0, y = 0)

name = Label(root, text = "Translator", fg = "#FFFFFF", bd = 0, bg="#011226")
name.config(font=("Transformers Movie", 30))
name.pack(pady = 10)

box = Text(root, width = 28, height = 8, font = ("ROBOTO", 16))
box.pack(pady = 20)
box1 = Text(root, width = 28, height = 8, font = ("ROBOTO", 16))
box1.pack(pady = 50)

button_frame = Frame(root).pack(side = BOTTOM)

def clear():
	box.delete(1.0,END)
	box1.delete(1.0,END)
def translate():
	INPUT = box.get(1.0,END)
	print(INPUT)
	t = Translator()
	a = t.translate(INPUT, src='vi', dest='en')
	b = a.text
	box1.insert(END,b)

clear_button = Button(button_frame, text = "Clear text", font = (("Arial"), 10, 'bold'), bg = '#303030', fg = '#FFFFFF', command = clear)
clear_button.place(x = 130, y = 310)
trans_button = Button(button_frame, text = "Translate text", font = (("Arial"), 10, 'bold'), bg = '#303030', fg = '#FFFFFF', command = translate)
trans_button.place(x = 300, y = 310)

root.mainloop()