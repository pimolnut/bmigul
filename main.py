from tkinter import *
import math

def leftClickButton(event):
    bmi = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)
    format_float = "{:.2f}".format(bmi)
    labelResult.configure(text = format_float)
    print(format_float)
    if bmi >= 30.0:
        labalbmi.configure(text = "so fat")
    elif 25.0 <= bmi <= 29.9:
        labalbmi.configure(text = "fat")
    elif 23.0 <= bmi <= 24.9:
        labalbmi.configure(text = "over")
    elif 18.6 <= bmi <= 22.9:
        labalbmi.configure(text = "normal")
    elif bmi <= 18.5 :
        labalbmi.configure(text = "underweight")

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
labalbmi = Label(MainWindow,text = "bmi")
labalbmi.grid(row=3,column=1)

MainWindow.mainloop()