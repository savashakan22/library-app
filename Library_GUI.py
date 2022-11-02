from tkinter import Label, Tk, Text, Entry, Button, END
import Library_Class as lc

root = Tk()
root.geometry("850x400")
root.title("School Library")

def takebook():
    lc.Member(Name_entry.get(), Lastname_entry.get()).addbook(Bookno_entry.get(), Bookname_entry.get())
    Bookname_entry.delete(0, 'end')
    Bookno_entry.delete(0, 'end')

def returnbook():
    lc.Member(Name_entry.get(), Lastname_entry.get()).returnbook(Return_bookno_entry.get())

    Return_bookno_entry.delete(0, 'end')


def showbook():
    kitaptext = lc.Member(Name_entry.get(), Lastname_entry.get()).showbook()

    Book_dataframe.delete(1.0, END)
    Book_dataframe.insert(END, str(kitaptext))
    Book_dataframe.place(y=80, x= 400)

#-* Member name labels *-#
Name_text = Label(root, text= "Name")
Name_text.place(x=400, y= 10)

Lastname_text = Label(root, text = "Lastname")
Lastname_text.place(x=550, y=10)
#-**-#

#-* Member name and lastname entry *-#
Name_entry = Entry(root, bd = 2)
Name_entry.place(x=400, y= 35)

Lastname_entry = Entry(root, bd = 2)
Lastname_entry.place(x=550, y= 35)
#-**-#

#-* Booknumber label and entry *-#
Bookno_text = Label(root, text = "Book No: ")
Bookno_text.place(x=10, y=60)

Bookno_entry = Entry(root, bd = 3)
Bookno_entry.place(x=10, y=90)
#-**-#

#-* Bookname label and entry *-#
Bookname_text = Label(root, text = "Book Name: ")
Bookname_text.place(x=10, y=10)

Bookname_entry = Entry(root, bd = 3)
Bookname_entry.place(x= 10, y=30)
#-**-#

#-* Button for adding books to a register *-#
Take_button = Button(root, text = "Add book", command = takebook)
Take_button.place(x=140, y=91)
#-**-#

#-* Label, Entry and Button for returning a book *-#
Return_bookno_text = Label(root, text = "Returning Book Number")
Return_bookno_text.place(x=10, y=200)

Return_bookno_entry = Entry(root, bd = 3)
Return_bookno_entry.place(x=10, y=230)

Return_book_button = Button(root, text = "Return Book", command = returnbook)
Return_book_button.place(x=140, y=231)
#-**-#

#-* Button for showing book records of a register *-#
Show_book_button = Button(root, text = "Show books", command = showbook)
Show_book_button.place(x=265, y=100)
#-**-# 

#-* Instructions text *-#
Instruction_text = Label(root, text = "Enter Name and Lastname\n To Add a book enter bookname and number and press the button\n To return a book enter return bookname and press the button \n Use the Show books to show the books of the student")
Instruction_text.place(x=10, y=290)
#-**-#

Book_dataframe = Text(root)

root.mainloop()