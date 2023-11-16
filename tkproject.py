import tkinter as tk
import tkinter.font as tkf

window = tk.Tk()
window.geometry("600x400+100+100")
window.resizable(1,1)
window.attributes('-fullscreen',True)

label=tk.Label(window,text="Test")
label.pack()

aa=["123","234"]

ffontl = tkf.Font(size=50,weight='bold')
ffontb = tkf.Font(size=20,weight='bold')
def showInput(event):
    a=str(textExample.get())[1:12]
    result="Patron ID : "+a
    label.config(text=result)
    if a in aa:
        global new
        new = tk.Toplevel(bg="green")
        newlabel=tk.Label(new,text="PASS",fg="white",height=6,background="green",font=ffontl)
        newlabel.pack()
        new.attributes('-fullscreen',True)
        newbtn=tk.Button(new,text="OK",command=deleteInput,width=7,font=ffontb,background="white",relief="raised")
        newbtn.pack()
    else:
        new=tk.Toplevel(bg="red")
        newlabel=tk.Label(new,text="Try Again",fg="white",height=6,background="red",font=ffontl)
        newlabel.pack()
        new.attributes('-fullscreen',True)
        newbtn=tk.Button(new,text="OK",command=deleteInput,width=7,font=ffontb,background="white",relief="raised")
        newbtn.pack()

def deleteInput():
    new.destroy()
    textExample.delete(0,"end")
    
  
textExample = tk.Entry(window, width=40)
textExample.bind("<Return>",showInput)
textExample.pack()


label=tk.Label(window)
label.pack()

textlabel = tk.Label(window,text="Welcome",width=20,height=5,anchor="center",background="pink")
textlabel.pack()

window.mainloop()
