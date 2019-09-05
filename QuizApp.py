import tkinter as tk
from tkinter import ttk
LARGEFONT=("Impact",72)
SMALLFONT=("Verdana",18)
qNa=(("a",1,2,3,4),("b",1,2,3))
class QuizApp():
    def __init__(self,parent):
        self.v = tk.IntVar()
        self.v.set(1)

        rb_list=[]
        for i in qNa[1[]]:
            rb = tk.Radiobutton(parent, variable = self.v, value = i, text = "Option One")
            rb_list.append(rb)
            rb.pack()
        label1 = tk.Label(parent, textvariable = self.v) #tkinter converts IntVar to text for textvariable

        label1.pack()

        
        
if __name__ == "__main__":
    root=tk.Tk()
    app=QuizApp(root)
    root.mainloop
