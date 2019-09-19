#Btn=Button cmd=command
import tkinter as tk
LARGEFONT=("Impact",72)
SMALLFONT=("Verdana",18)

class QuizApp():
    def __init__(self,parent):    
        self.qNa=(("a","1","2","ey man","4"),("b","1","2","3"))#List of questions and answers
        self.correctanswers=("ey man","1")
        self.v = tk.StringVar()#Variable for radiobuttons
        self.radiobtnsframe=0
        self.page=0
        self.v.set("n/a")
        self.rblist=[]
        self.attemptlist=[]        
        self.radio_btn_gen()

        self.rightlabel=tk.Label(font=SMALLFONT)
        self.wronglabel=tk.Label(font=SMALLFONT)

        self.confirmlabel = tk.Label(parent, textvariable = self.v) #tkinter converts IntVar to text for textvariable
        self.confirmlabel.grid(row=1,column=0)

        nxtbtn=tk.Button(text="Next",font=SMALLFONT,command=self.nxt_btn_cmd)
        nxtbtn.grid(row=2,column=0)

        backbtn=tk.Button(text="Back",font=SMALLFONT,command=self.back_btn_cmd)
        backbtn.grid(row=3,column=0)

        resetbtn=tk.Button(text="Reset",font=SMALLFONT,command=self.reset_btn_cmd)
        resetbtn.grid(row=4,column=0)
    def radio_btn_gen(self):
        self.radiobtnsframe=tk.Frame(relief="flat",borderwidth=2)
        for i in self.qNa[self.page][1:]:#Iterates through inner lists of qNa 
            self.rb = tk.Radiobutton(master=self.radiobtnsframe,variable = self.v, value = i, text= i,indicatoron=False)
            self.rblist.append(self.rb)
            self.rb.pack(fill="both")
            self.radiobtnsframe.grid(row=0,column=0)
        self.v.set("n/a")

    def nxt_btn_cmd(self):
        rbValue=self.v.get()
        if rbValue != "n/a":
            self.page+=1
            print(self.page)
            if self.page+1 > len(self.qNa):
                correctattempts=[i for i, j in zip(self.attemptlist, self.correctanswers) if i == j]
                wrongattempts=[i for i, j in zip(self.attemptlist, self.correctanswers) if i != j]
                self.rightlabel.config(text="you got {} questions right".format(len(correctattempts)))
                self.wronglabel.config(text="you got {} questions right".format(len(wrongattempts)))
                self.rightlabel.grid(row=0,column=1)
                self.wronglabel.grid(row=0,column=2)
                self.radiobtnsframe.destroy()
                self.confirmlabel.destroy()
                return
            self.attemptlist.append(rbValue)
            self.radiobtnsframe.destroy()
            self.radio_btn_gen()
        del self.rblist[:]
        print(self.rblist)

    def back_btn_cmd(self):
        if self.page!=0:
            del self.attemptlist[-1] 
            self.page+=-1
            self.radiobtnsframe.destroy()
            self.radio_btn_gen()

    def reset_btn_cmd(self):
        self.radiobtnsframe.destroy()
        del self.attemptlist[:]
        self.page=0
        self.radio_btn_gen()


if __name__ == "__main__":
    root=tk.Tk()
    app=QuizApp(root)
    root.mainloop
