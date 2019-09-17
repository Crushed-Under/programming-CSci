import tkinter as tk
from tkinter import ttk
LARGEFONT=("Impact",72)
SMALLFONT=("Verdana",18)

class QuizApp():
    def __init__(self,parent):
        self.v = tk.IntVar()
        self.v.set(1)
        self.qNa=(("a",1,2,3,4),("b",1,2,3))
        self.cnter=0
        rb_list=[]
        while True:
            if self.cnter == len(self.qNa):
                for i in self.qNa[self.cnter][1:]:
                    rb = tk.Radiobutton(parent, variable = self.v, value = i, textvariable= i)
                    rb_list.append(rb)
                    rb.pack()
                self.cntr+=1
                btn1=tk.Button(text="Next",font=SMALLFONT,command=)
            else:
                break
        label1 = tk.Label(parent, textvariable = self.v) #tkinter converts IntVar to text for textvariable

        label1.pack()

        
        
if __name__ == "__main__":
    root=tk.Tk()
    app=QuizApp(root)
    root.mainloop
