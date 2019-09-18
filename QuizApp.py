#Btn=Button cmd=command
import tkinter as tk
LARGEFONT=("Impact",72)
SMALLFONT=("Verdana",18)

class QuizApp():
    def __init__(self,parent):    
        self.cnter=0 #Counter for iterating through questions
        self.qNa=(("a","1","2","ey man","4"),("b","1","2","3"))#List of questions and answers
        self.v = tk.StringVar()#Variable for radiobuttons
        self.v.set("l")
        self.rb_list=[]
        self.attemptlist=[]
        for i in self.qNa[self.cnter][1:]:#Iterates through inner lists of qNa 
            self.rb = tk.Radiobutton(parent, variable = self.v, value = i, textvariable= i)
            self.rb_list.append(self.rb)
            self.rb.pack()
        label1 = tk.Label(parent, textvariable = self.v) #tkinter converts IntVar to text for textvariable
        label1.pack()
        nextbutton=tk.Button(text="Next",font=SMALLFONT,command=self.NextButtoncmd)
        nextbutton.pack()
        
    def NextButtoncmd(self):
        a=self.v.get()
        self.attemptlist.append(a)
        print(self.v)
        print(self.attemptlist)

if __name__ == "__main__":
    root=tk.Tk()
    app=QuizApp(root)
    root.mainloop
