import tkinter as tk
window = tk.Tk()

window.geometry("600x400+100+100")
window.resizable(1,1)

label=tk.Label(window,text="Test")
label.pack()

def getTextInput():
    result=str(textExample.get())
    #print(result)
    label.configure(text=result)

def showInput(event):
    result="Patron ID : "+str(textExample.get())[1:12]
    label.config(text=result)

textExample = tk.Entry(window, width=40)
textExample.bind("<Return>",showInput)
textExample.pack()


label=tk.Label(window)
label.pack()

window.mainloop()
