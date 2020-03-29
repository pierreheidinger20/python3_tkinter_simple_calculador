from tkinter import *
import parser

root = Tk()
root.title("calculator")

display = Entry(root)

display.grid(row=1,columnspan=6,sticky=W+E)

# getNumber
i=0
def getNumbers(number):
    global i
    display.insert(i,number)
    i+=1
def getOperation(operation):
    global i
    operator_length = len(operation)
    display.insert(i,operation)
    i+=operator_length

def clearDisplay():
    display.delete(0,END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clearDisplay()
        display.insert(0,display_new_state)
    else:
        clearDisplay()

def calculate():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clearDisplay()
        display.insert(0,result)
    except:
        clearDisplay()
        display.insert(0,'Error')

# Numbers
Button(root,text="1",command=lambda:getNumbers(1)).grid(row=2,column=0)
Button(root,text="2",command=lambda:getNumbers(2)).grid(row=2,column=1)
Button(root,text="3",command=lambda:getNumbers(3)).grid(row=2,column=2)

Button(root,text="4",command=lambda:getNumbers(4)).grid(row=3,column=0)
Button(root,text="5",command=lambda:getNumbers(5)).grid(row=3,column=1)
Button(root,text="6",command=lambda:getNumbers(6)).grid(row=3,column=2)

Button(root,text="7",command=lambda:getNumbers(7)).grid(row=4,column=0)
Button(root,text="8",command=lambda:getNumbers(8)).grid(row=4,column=1)
Button(root,text="9",command=lambda:getNumbers(9)).grid(row=4,column=2)

Button(root,text="0",command=lambda:getNumbers(0)).grid(row=5,column=1)

# Operations
Button(root,text="AC",command=lambda:clearDisplay()).grid(row=5,column=0)
Button(root,text="%",command=lambda:getOperation("%")).grid(row=5,column=2)

Button(root,text="+",command=lambda:getOperation("+")).grid(row=2,column=3)
Button(root,text="-",command=lambda:getOperation("-")).grid(row=3,column=3)
Button(root,text="x",command=lambda:getOperation("*")).grid(row=4,column=3)
Button(root,text="/",command=lambda:getOperation("/")).grid(row=5,column=3)

Button(root,text="del",command=lambda:undo()).grid(row=2,column=4,columnspan=2,sticky=W+E)
Button(root,text="exp",command=lambda:getOperation("**")).grid(row=3,column=4,sticky=W+E)
Button(root,text="^2",command=lambda:getOperation("**2")).grid(row=3,column=5,sticky=W+E)
Button(root,text="(",command=lambda:getOperation("(")).grid(row=4,column=4,sticky=W+E)
Button(root,text=")",command=lambda:getOperation(")")).grid(row=4,column=5,sticky=W+E)
Button(root,text="=",command=lambda:calculate()).grid(row=5,column=4,columnspan=2,sticky=W+E)


root.mainloop()