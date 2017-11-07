from tkinter import *


def find_isbn(isbn, lbl):
    if len(isbn) == 10:
        mult = 11
        total = 0
        for i in range(len(isbn)):
            total += int(isbn[i]) * mult
            mult -= 1
        digit_11 = 11 - (total % 11)
        if digit_11 == 10:
            digit_11 = 'X'
        isbn += str(digit_11)
        lbl.config(text=isbn)
    elif len(isbn) > 10 :
        messagebox.showinfo(title="Error Message", message="You must input 10 digits - no more, no less NOT string(letters)")
        return
    elif len(isbn) < 10:
        messagebox.showinfo(title="Error Message", message="You must input 10 digits - no more, no less NOT string(letters)")
        return

top = Tk()
top.geometry("450x150+500+300")
top.title("Ahmed's ISBN generator")

button = Button(top, text="OK", command=lambda: find_isbn(mEntry.get(), mlabel2))
button.pack()

label = Label(top, text="Please enter the 10 digit number")
label.pack()

error_label = Label(top, text="Please enter integer(numbers)")


class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Close'
        self['command'] = parent.destroy
        self.pack(side=BOTTOM)


quitButton(top)

mEntry = Entry(top)    
mEntry.pack()

mlabel2 = Label(top, text='')
mlabel2.pack()

top.mainloop()
