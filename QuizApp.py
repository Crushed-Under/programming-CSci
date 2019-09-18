#Btn=Button cmd=command
import tkinter as tk
LARGEFONT=("Impact",72)
SMALLFONT=("Verdana",18)

class QuizApp():
    def __init__(self,parent):    
        self.cnter=0 #Counter for iterating through questions
        self.qNa=(("a","1","2","ey man","4"),("b","1","2","3"))#List of questions and answers
        self.v = tk.StringVar()#Variable for radiobuttons
        self.radiobtnsframe=0
        self.page=0
        self.v.set("n/a")
        self.rb_list=[]
        self.attemptlist=[]
        
        self.radioBtnGen()
        label1 = tk.Label(parent, textvariable = self.v) #tkinter converts IntVar to text for textvariable
        label1.grid(row=1,column=0)
        nxtbtn=tk.Button(text="Next",font=SMALLFONT,command=self.nxt_btn_cmd)
        nxtbtn.grid(row=2,column=0)

    def radioBtnGen(self):
        self.radiobtnsframe=tk.Frame(relief="flat",borderwidth=2)
        for i in self.qNa[self.page][1:]:#Iterates through inner lists of qNa 
            self.rb = tk.Radiobutton(master=self.radiobtnsframe,variable = self.v, value = i, text= i)
            self.rb_list.append(self.rb)
            self.rb.pack()
            self.radiobtnsframe.grid(row=0,column=0)

    def nxt_btn_cmd(self):
        rbValue=self.v.get()
        if rbValue != "n/a":
            self.page+=1
            self.attemptlist.append(rbValue)
            self.radiobtnsframe.destroy()
            self.radioBtnGen()
        del self.rb_list[:]
        print(self.rb_list)
        print(self.page)#4 debug

    """def back_btn_cmd(self):
        if self.page!=0:
            del self.attemptlist[-1] 
            self.page+=-1
            print(self.page)#4 debug
        else:
            pass"""
if __name__ == "__main__":
    root=tk.Tk()
    app=QuizApp(root)
    root.mainloop
