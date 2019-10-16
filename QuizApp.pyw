#Btn=Button cmd=command
import tkinter as tk
LARGEFONT=("Impact",72)
SMALLFONT=("Verdana",12)

class QuizApp():
    def __init__(self,parent):    
        self.qNa=(("What is the capital city of Puerto Rico","San Juan","Tiquana","Honduras"),
        ("What is the world's third largest sea?","The Mediterranean","The Tasman","The Black sea","The Caspian Sea"),
        (" What is the capital of Qatar?","Abu Dubi","Dubai","Asur","Nineva","Doha"), 
        ("In which South American country is the Atacama desert?","Paraguay","Argentina","Chile","Ecuador"),
        ("What is the least populated state in the US","Kansas","Missisipi","Wyoming")
        )#List of questions and answers
        self.correctanswers=("San Juan","The Mediterranean","Doha","Chile","Wyoming")#All the correct answers
        self.v = tk.StringVar()#Variable for radiobuttons
        self.page=0
        self.radiobtnsframe=0
        self.v.set("n/a")
        self.rblist=[]
        self.attemptlist=[]        

        self.questionvar=tk.StringVar()
        self.questionlabel=tk.Label(parent,textvariable=self.questionvar,font=SMALLFONT)
        self.questionlabel.grid(row=0,column=0)

        self.rightlabel=tk.Label(font=SMALLFONT)
        self.wronglabel=tk.Label(font=SMALLFONT)

        self.confirmlabel = tk.Label(parent, textvariable = self.v) #tkinter converts IntVar to text for textvariable
        self.confirmlabel.grid(row=1,column=1)

        self.nxtbtn=tk.Button(text="Next",font=SMALLFONT,command=self.nxt_btn_cmd)
        self.nxtbtn.grid(row=4,column=0)

        self.backbtn=tk.Button(text="Back",font=SMALLFONT,command=self.back_btn_cmd)
        self.backbtn.grid(row=5,column=0)

        self.resetbtn=tk.Button(text="Reset",font=SMALLFONT,command=self.reset_btn_cmd)
        self.resetbtn.grid(row=6,column=0)
        self.radio_btn_gen()

    def labelinit(self):
        self.rightlabel=tk.Label(font=SMALLFONT)
        self.wronglabel=tk.Label(font=SMALLFONT)
        self.questionlabel=tk.Label(textvariable=self.questionvar,font=SMALLFONT)

    def radio_btn_gen(self):
        self.questionvar.set(self.qNa[self.page][0])
        self.radiobtnsframe=tk.Frame(relief="flat",borderwidth=2)
        for i in self.qNa[self.page][1:]:#Iterates through inner lists of qNa
            self.rb = tk.Radiobutton(master=self.radiobtnsframe,variable = self.v, value = i, 
            text= i,indicatoron=False,font=SMALLFONT)
            self.rblist.append(self.rb)
            self.rb.pack(fill="both")
            self.radiobtnsframe.grid(row=1,column=0)
        self.v.set("n/a")
        
    def nxt_btn_cmd(self):
        rbValue=self.v.get()
        if rbValue != "n/a":
            self.page+=1
            print(self.page)
            self.attemptlist.append(rbValue)
            if self.page+1 > len(self.qNa):
                correctattempts=[i for i, j in zip(self.attemptlist, self.correctanswers) if i == j]
                wrongattempts=[i for i, j in zip(self.attemptlist, self.correctanswers) if i != j]
                print(correctattempts)
                print(wrongattempts)
                self.rightlabel.config(text="you got {} questions right".format(len(correctattempts)))
                self.wronglabel.config(text="you got {} questions wrong".format(len(wrongattempts)))
                self.rightlabel.grid(row=0,column=0)
                self.wronglabel.grid(row=1,column=0)
                self.questionlabel.destroy()
                self.radiobtnsframe.destroy()
                self.confirmlabel.destroy()
                return
            self.radiobtnsframe.destroy()
            self.radio_btn_gen()
        del self.rblist[:]

    def back_btn_cmd(self):
        if self.page!=0:
            if self.page+1 > len(self.qNa):
                self.rightlabel.destroy()
                self.wronglabel.destroy()
            del self.attemptlist[-1] 
            self.page+=-1
            self.radiobtnsframe.destroy()
            self.radio_btn_gen()
            self.questionlabel.grid(row=0,column=0)
    def reset_btn_cmd(self):
        self.radiobtnsframe.destroy()
        self.rightlabel.destroy()
        self.wronglabel.destroy()
        del self.attemptlist[:]
        self.page=0
        self.radio_btn_gen()
        self.questionlabel.grid(row=0,column=0)

if __name__ == "__main__":
    root=tk.Tk()
    app=QuizApp(root)
    root.mainloop