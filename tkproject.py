import tkinter as tk
import tkinter.font as tkf


window = tk.Tk()
window.resizable(1,1)
window.attributes('-fullscreen',True)
window['bg']="#0B0B3B"

#font
ffontl = tkf.Font(size=50,weight='bold')
ffontb = tkf.Font(size=20,weight='bold')

label=tk.Label(window,text="Test",font=ffontl,padx = 20, pady = 30,fg="white",background="#0B0B3B")
label.pack()

aa=["88800248001","aaa"]


def showInput(event):
    a=str(textExample.get())[1:12]
    result="Patron ID : "+a
    # label.config(text=result)
    if a in aa:
        global new
        new = tk.Toplevel(bg="green")
        newlabel=tk.Label(new,text="Welcome!",fg="white",height=6,background="green",font=ffontl)
        newlabel.pack()
        new.attributes('-fullscreen',True)
        newbtn=tk.Button(new,text="OK",command=deleteInput,width=7,font=ffontb,background="white",relief="raised")
        newbtn.pack()
    else:
        new=tk.Toplevel(bg="red")
        newlabel=tk.Label(new,text="Invalid Card",fg="white",height=6,background="red",font=ffontl)
        newlabel.pack()
        new.attributes('-fullscreen',True)
        
        newbtn=tk.Button(new,text="OK",command=deleteInput,width=7,font=ffontb,background="white",relief="raised")
        newbtn.pack()

def deleteInput():
    new.destroy()
    textExample.delete(0,"end")
    
  
textExample = tk.Entry(window, width=40,font=ffontb)
textExample.bind("<Return>",showInput)
textExample.pack()


# label=tk.Label(window)
# label.pack()

textlabel = tk.Label(window,text="Welcome!",anchor="center",background="#0B0B3B",font=ffontl,fg="white")
textlabel.pack(padx = 20, pady = 30)

photo=tk.PhotoImage(file="media/example.PNG")
photolabel = tk.Label(window,image=photo)
photolabel.pack()



window.mainloop()
