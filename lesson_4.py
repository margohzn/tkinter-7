#creating message box 

from tkinter import * 
from tkinter.ttk import * 
from tkinter.filedialog import askopenfile

window = Tk()
window.geometry("300x200")
window.title("message box")

def open_file():
    file = askopenfile(mode = "r", filetypes = [("Python Files", "*.py")]) #r = reading 
    if file is not None:
        content = file.read()
        print(content)

button = Button(window, text = "Open file", command = lambda:open_file()).place(x = 150, y = 100)



window.mainloop()