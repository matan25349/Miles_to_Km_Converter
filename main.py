from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
# Label
my_label1 = Label(text="is eqaul to", font=("Arial", 15, "bold"))
my_label1.grid(row=1, column=0)
my_label2 = Label(text="Miles", font=("Arial", 15, "bold"))
my_label2.grid(row=0, column=2)
my_label3 = Label(text="Km", font=("Arial", 15, "bold"))
my_label3.grid(row=1, column=2)


# Button
def button_clicked():
    miles = float(input1.get())
    km = miles * 1.609
    input2.insert(END,str(km))
   

def reset():
    input1.delete(0, END)
    input2.delete(0, END)


button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)
button2 = Button(text="Reset", command=reset)
button2.grid(row=3, column=1)

input1 = Entry(width=10)
input1.grid(row=0, column=1)
input1.insert(0, "0")
input2 = Entry(width=10)
input2.insert(0, "0")
input2.grid(row=1, column=1)
window.mainloop()
