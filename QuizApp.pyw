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
        self.radbtnvar = tk.StringVar()#Variable for radiobuttons
        self.page=0
        self.v=tk.StringVar()
        self.v.set("n/a")
        self.rblist=[]#stores all the attempts made on the quiz        
        self.attemptlist=[]        
        #above are the variables used for managing the radio button list
        self.questionvar=tk.StringVar()
        self.questionlabel=tk.Label(parent,textvariable=self.questionvar,font=SMALLFONT)
        self.questionlabel.grid(row=0,column=0)

        self.rightlabel=tk.Label(font=SMALLFONT)#Displays correct answers at the end of quiz
        self.wronglabel=tk.Label(font=SMALLFONT)#Displays wrong answers at the end of quiz

        self.confirmlabel = tk.Label(parent, textvariable = self.radbtnvar) #tkinter converts IntVar to text for textvariable
        self.confirmlabel.grid(row=1,column=1)

        self.nxtbtn=tk.Button(text="Next",font=SMALLFONT,command=self.nxt_btn_cmd)#next button
        self.nxtbtn.grid(row=4,column=0)

        self.backbtn=tk.Button(text="Back",font=SMALLFONT,command=self.back_btn_cmd)#back button
        self.backbtn.grid(row=5,column=0)

        self.resetbtn=tk.Button(text="Reset",font=SMALLFONT,command=self.reset_btn_cmd)#reset button
        self.resetbtn.grid(row=6,column=0)
        self.radio_btn_gen()
        

    def radio_btn_gen(self):
        self.questionvar.set(self.qNa[self.page][0])#Creates the question label in the gui
        self.radiobtnsframe=tk.Frame(relief="flat",borderwidth=2)# the frame that holds the radiobuttons
        for i in self.qNa[self.page][1:]:#Iterates through inner lists of 'qNa' list and loads the radiobuttons into 'radiobtnsframe' 
            self.rb = tk.Radiobutton(master=self.radiobtnsframe,variable = self.v, value = i, 
            text= i,indicatoron=False,font=SMALLFONT)
            self.rblist.append(self.rb)
            self.rb.pack(fill="both")
            self.radiobtnsframe.grid(row=1,column=0)
        self.radbtnvar.set("n/a")
        
    def nxt_btn_cmd(self):#command called when next button pushed
        rbValue=self.v.get()#calls 'v' and assigns it to rbValue
        if rbValue != "n/a":#checks to see if any radiobuttons have been pushed
            self.page+=1#increments page number
            print(self.page)
            self.attemptlist.append(rbValue)
            if self.page+1 > len(self.qNa):#checks to see if page number matches the number of questions 
                correctattempts=[i for i, j in zip(self.attemptlist, self.correctanswers) if i == j]#used to sort the correct answers into a list
                wrongattempts=[i for i, j in zip(self.attemptlist, self.correctanswers) if i != j]
                print(correctattempts)
                print(wrongattempts)
                self.rightlabel.config(text="you got {} questions right".format(len(correctattempts)))#displays how many answers you got right
                self.wronglabel.config(text="you got {} questions wrong".format(len(wrongattempts)))#displays how many answers you got wrong
                self.rightlabel.grid(row=0,column=0)
                self.wronglabel.grid(row=1,column=0)
                self.questionlabel.grid_remove()
                self.radiobtnsframe.destroy() 
                self.confirmlabel.grid_remove()
                return#terminates method before executing the commands below \
            self.radiobtnsframe.destroy()
            self.radio_btn_gen()
        del self.rblist[:]#clears the list storing the radiobutton data

    def back_btn_cmd(self):
        if self.page!=0:
            if self.page+1 > len(self.qNa):
                self.rightlabel.grid_remove()
                self.wronglabel.grid_remove()
            del self.attemptlist[-1] 
            self.page+=-1
            self.radiobtnsframe.destroy()
            self.radio_btn_gen()
            self.questionlabel.grid(row=0,column=0)
    def reset_btn_cmd(self):
        self.radiobtnsframe.destroy()
        self.rightlabel.grid_remove()
        self.wronglabel.grid_remove()
        del self.attemptlist[:]
        self.page=0
        self.radio_btn_gen()
        self.questionlabel.grid(row=0,column=0)

if __name__ == "__main__":
    root=tk.Tk()
    app=QuizApp(root)   
    root.columnconfigure(0, minsize=550)
    root.mainloop
