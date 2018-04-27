# ROSHAN SAGANTI
# HYUNSOO KIM

# EXTERNAL LIBRARIES
try:
    from Tkinter import * # this is for python2
except:
    from tkinter import * # this is for python3

class Application(Frame):
    # GLOBAL VARIABLES
    isDivide=False
    isMultiply=False
    isSubtract=False
    isAdd=False
    isSolution=False
    
    # METHODS
    def clear(self):
        global isDivide
        #self.operationView.config(text="")
        self.mainView.config(text="0")
        self.add.config(state="normal")
        self.plusMinus.config(state="disabled")
        self.percent.config(state="disabled")

        if (self.isDivide):
            self.isDivide=False

        self.isMultiply=False
        self.isSubtract=False
        self.isAdd=False
        self.isSolution=False

    def doEquals(self):
        var2 = self.mainView.cget("text")

        if(self.isDivide):
            divSolution = float(var1) / float(var2)
            #self.operationView["text"] = (var1," + ",var2," = "),int(addSolution)
            self.mainView.config(text=divSolution)
            self.divide.config(state="normal")
            self.isDivide=False

        if(self.isMultiply):
            mulSolution = float(var1) * float(var2)
            #self.operationView["text"] = (var1," + ",var2," = "),int(addSolution)
            self.mainView.config(text=mulSolution)
            self.multiply.config(state="normal")
            self.isMultiply=False

        if(self.isSubtract):
            subSolution = float(var1) - float(var2)
            #self.operationView["text"] = (var1," + ",var2," = "),int(addSolution)
            self.mainView.config(text=subSolution)
            self.minus.config(state="normal")
            self.isSubtract=False

        if(self.isAdd):
            addSolution = float(var1) + float(var2)
            #self.operationView["text"] = (var1," + ",var2," = "),int(addSolution)
            self.mainView.config(text=addSolution)
            self.add.config(state="normal")
            self.isAdd=False

    # CHANGE THE SIGN FROM NEGATIVE TO POSTIVE AND VICE VERSA
    # OF DIGITS ONLY EXISTING IN mainView
    def changeSign(self):
        global var1
        var1 = self.mainView.cget("text")

        sol = float(var1) * -1

        self.mainView.config(text=sol)

    def takePercent(self):
        global var1
        var1 = self.mainView.cget("text")

        perSolution = float(var1) / 100
        self.mainView.config(text=perSolution)

    def doDivision(self):
        #global self.isDivide
        self.isDivide=True

        global var1
        var1 = self.mainView.cget("text")

        #self.operationView.config(text=var1 + " + ")
        self.mainView.config(text="0")
        #self.divide.config(state="disabled")

    def doMultiplication(self):
        self.isMultiply=True

        global var1
        var1 = self.mainView.cget("text")

        #self.operationView.config(text=var1 + " + ")
        self.mainView.config(text="0")
        self.multiply.config(state="disabled")

    def doSubtraction(self):
        self.isSubtract=True

        global var1
        var1 = self.mainView.cget("text")

        #self.operationView.config(text=var1 + " + ")
        self.mainView.config(text="0")
        self.minus.config(state="disabled")

    def doAddition(self):
        #global self.isAdd
        self.isAdd=True

        global var1
        var1 = self.mainView.cget("text")

        #self.operationView.config(text=var1 + " + ")
        self.mainView.config(text="0")
        self.add.config(state="disabled")

    def printOne(self):
        if "0" in self.mainView.cget("text"):
            if len(self.mainView.cget("text")) == 1:
                    self.mainView.config(text="1")
                    self.plusMinus.config(state="normal")
                    self.percent.config(state="normal")
            elif len(self.mainView.cget("text")) > 1:
                    self.mainView.config(text=self.mainView.cget("text") + "1")
        else:
            self.mainView.config(text=self.mainView.cget("text") + "1")

    def printTwo(self):
        if "0" in self.mainView.cget("text"):
            if len(self.mainView.cget("text")) == 1:
                    self.mainView.config(text="2")
                    self.plusMinus.config(state="normal")
                    self.percent.config(state="normal")
            elif len(self.mainView.cget("text")) > 1:
                    self.mainView.config(text=self.mainView.cget("text") + "2")
        else:
            self.mainView.config(text=self.mainView.cget("text") + "2")

    def printThree(self):
        if "0" in self.mainView.cget("text"):
            if len(self.mainView.cget("text")) == 1:
                    self.mainView.config(text="3")
                    self.plusMinus.config(state="normal")
                    self.percent.config(state="normal")
            elif len(self.mainView.cget("text")) > 1:
                {
                    self.mainView.config(text=self.mainView.cget("text") + "3")
                }
        else:
            self.mainView.config(text=self.mainView.cget("text") + "3")

    def printFour(self):
        if "0" in self.mainView.cget("text"):
            if len(self.mainView.cget("text")) == 1:
                    self.mainView.config(text="4")
                    self.plusMinus.config(state="normal")
                    self.percent.config(state="normal")
            elif len(self.mainView.cget("text")) > 1:
                {
                    self.mainView.config(text=self.mainView.cget("text") + "4")
                }
        else:
            self.mainView.config(text=self.mainView.cget("text") + "4")

    def printFive(self):
        if "0" in self.mainView.cget("text"):
            if len(self.mainView.cget("text")) == 1:
                    self.mainView.config(text="5")
                    self.plusMinus.config(state="normal")
                    self.percent.config(state="normal")
            elif len(self.mainView.cget("text")) > 1:
                {
                    self.mainView.config(text=self.mainView.cget("text") + "5")
                }
        else:
            self.mainView.config(text=self.mainView.cget("text") + "5")

    def printSix(self):
        if "0" in self.mainView.cget("text"):
            if len(self.mainView.cget("text")) == 1:
                    self.mainView.config(text="6")
                    self.plusMinus.config(state="normal")
                    self.percent.config(state="normal")
            elif len(self.mainView.cget("text")) > 1:
                {
                    self.mainView.config(text=self.mainView.cget("text") + "6")
                }
        else:
            self.mainView.config(text=self.mainView.cget("text") + "6")

    def printSeven(self):
        if "0" in self.mainView.cget("text"):
            if len(self.mainView.cget("text")) == 1:
                    self.mainView.config(text="7")
                    self.plusMinus.config(state="normal")
                    self.percent.config(state="normal")
            elif len(self.mainView.cget("text")) > 1:
                {
                    self.mainView.config(text=self.mainView.cget("text") + "7")
                }
        else:
            self.mainView.config(text=self.mainView.cget("text") + "7")

    def printEight(self):
        if "0" in self.mainView.cget("text"):
            if len(self.mainView.cget("text")) == 1:
                    self.mainView.config(text="8")
                    self.plusMinus.config(state="normal")
                    self.percent.config(state="normal")
            elif len(self.mainView.cget("text")) > 1:
                {
                    self.mainView.config(text=self.mainView.cget("text") + "8")
                }
        else:
            self.mainView.config(text=self.mainView.cget("text") + "8")

    def printNine(self):
        if "0" in self.mainView.cget("text"):
            if len(self.mainView.cget("text")) == 1:
                    self.mainView.config(text="9")
                    self.plusMinus.config(state="normal")
                    self.percent.config(state="normal")
            elif len(self.mainView.cget("text")) > 1:
                {
                    self.mainView.config(text=self.mainView.cget("text") + "9")
                }
        else:
            self.mainView.config(text=self.mainView.cget("text") + "9")

    def printZero(self):
        if "0" in self.mainView.cget("text"):
            if len(self.mainView.cget("text")) == 1:
                    self.mainView.config(text="0")
            elif len(self.mainView.cget("text")) > 1:
                {
                    self.mainView.config(text=self.mainView.cget("text") + "0")
                }
        else:
            self.mainView.config(text=self.mainView.cget("text") + "0")

    def printDot(self):
        self.mainView.config(text=self.mainView.cget("text") + ".")

    def createWidgets(self):
        global calcView, opView

        # FIRST ROW OF BUTTONS 
        # AC(ALL CLEAR) BUTTON
        self.allClear = Button(self)
        self.allClear["text"] = "AC"
        #self.allClear["padx"]   = "10px"
        #self.allClear["pady"]   = "10px"
        #self.allClear["bg"]   = "grey"
        self.allClear["width"]   = 7
        self.allClear["height"]   = 2
        self.allClear["command"] =  self.clear

        # PLUS OR MINUS BUTTON
        self.plusMinus = Button(self)
        self.plusMinus["text"] = "+/-"
        self.plusMinus["width"]   = 7
        self.plusMinus["height"]   = 2
        self.plusMinus["command"] = self.changeSign
        self.plusMinus.config(state="disabled")

        # TAKE PERCENTAGE BUTTON
        self.percent = Button(self)
        self.percent['text'] = "%"
        self.percent["width"]   = 7
        self.percent["height"]   = 2
        self.percent['command'] = self.takePercent
        self.percent.config(state="disabled")

        # DIVISION BUTTON
        self.divide = Button(self)
        self.divide["text"] = "/"
        self.divide["width"]   = 7
        self.divide["height"]   = 2
        self.divide["bg"]   = "orange"
        self.divide["fg"]   = "white"
        self.divide["command"] =  self.doDivision

        self.multiply = Button(self)
        self.multiply["text"] = "X"
        self.multiply["width"]   = 7
        self.multiply["height"]   = 2
        self.multiply["bg"]   = "orange"
        self.multiply["fg"]   = "white"
        self.multiply["command"] =  self.doMultiplication

        self.minus = Button(self)
        self.minus["text"] = "-"
        self.minus["width"]   = 7
        self.minus["height"]   = 2
        self.minus["bg"]   = "orange"
        self.minus["fg"]   = "white"
        self.minus["command"] =  self.doSubtraction

        self.add = Button(self)
        self.add["text"] = "+"
        self.add["width"]   = 7
        self.add["height"]   = 2
        self.add["bg"]   = "orange"
        self.add["fg"]   = "white"
        self.add["command"] =  self.doAddition

        self.equals = Button(self)
        self.equals["text"] = "="
        self.equals["width"]   = 7
        self.equals["height"]   = 2
        self.equals["bg"]   = "orange"
        self.equals["fg"]   = "white"
        self.equals["command"] =  self.doEquals

        self.one = Button(self)
        self.one["text"] = "1"
        self.one["width"]   = 7
        self.one["height"]   = 2
        self.one["command"] =  self.printOne

        self.two = Button(self)
        self.two["text"] = "2"
        self.two["width"]   = 7
        self.two["height"]   = 2
        self.two["command"] =  self.printTwo

        self.three = Button(self)
        self.three["text"] = "3"
        self.three["width"]   = 7
        self.three["height"]   = 2
        self.three["command"] =  self.printThree

        self.four = Button(self)
        self.four["text"] = "4"
        self.four["width"]   = 7
        self.four["height"]   = 2
        self.four["command"] =  self.printFour

        self.five = Button(self)
        self.five["text"] = "5"
        self.five["width"]   = 7
        self.five["height"]   = 2
        self.five["command"] =  self.printFive

        self.six = Button(self)
        self.six["text"] = "6"
        self.six["width"]   = 7
        self.six["height"]   = 2
        self.six["command"] =  self.printSix

        self.seven = Button(self)
        self.seven["text"] = "7"
        self.seven["width"]   = 7
        self.seven["height"]   = 2
        self.seven["command"] =  self.printSeven

        self.eight = Button(self)
        self.eight["text"] = "8"
        self.eight["width"]   = 7
        self.eight["height"]   = 2
        self.eight["command"] =  self.printEight

        self.nine = Button(self)
        self.nine["text"] = "9"
        self.nine["width"]   = 7
        self.nine["height"]   = 2
        self.nine["command"] =  self.printNine

        self.zero = Button(self)
        self.zero["text"] = "0"
        self.zero["width"]   = 16
        self.zero["height"]   = 2
        self.zero["command"] =  self.printZero

        self.dot = Button(self)
        self.dot["text"] = "."
        self.dot["width"]   = 7
        self.dot["height"]   = 2
        self.dot["command"] =  self.printDot

        # GRID ALL THE BUTTONS TOGETHER
        #self.operationView = Label(self, text=opView, anchor="w", font=("Courier", 14))
        #self.operationView.grid(row=1,column=1)

        self.columnconfigure(1, weight=4)

        self.mainView = Label(self, text="0", anchor="e", height=4, bg="black", fg="white")
        self.mainView.grid(row=1,column=4,columnspan=4)

        self.allClear.grid(row=3,column=1)
        self.plusMinus.grid(row=3,column=2)
        self.percent.grid(row=3,column=3)
        self.divide.grid(row=3,column=4)

        self.seven.grid(row=4,column=1)
        self.eight.grid(row=4,column=2)
        self.nine.grid(row=4,column=3)
        self.multiply.grid(row=4,column=4)

        self.four.grid(row=5,column=1)
        self.five.grid(row=5,column=2)
        self.six.grid(row=5,column=3)
        self.minus.grid(row=5,column=4)

        self.one.grid(row=6,column=1)
        self.two.grid(row=6,column=2)
        self.three.grid(row=6,column=3)
        self.add.grid(row=6,column=4)

        self.zero.grid(row=7,column=1,columnspan=2)
        self.dot.grid(row=7,column=3)
        self.equals.grid(row=7,column=4)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.minsize(width=208,height=238)
        master.maxsize(width=208,height=238)
        master.bg="black"
        self.grid()
        self.createWidgets()

root = Tk()
root.title("Best Calculator v2.0")
app = Application(master=root)
app.configure(background="black")
app.mainloop()
root.quit()