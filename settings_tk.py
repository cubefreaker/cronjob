from tkinter import *
from tkinter import messagebox
import json
import sqlite3

window = Tk()
window.title("Autoprint Settings")
window.geometry("300x250")

branchLabel = Label(window, text="Branch")
branchLabel.grid(column=0, row=0)

conn = sqlite3.connect('data.db')
c = conn.cursor()


c.execute('SELECT isChecked FROM settings where branchCode="013"')
val1 = c.fetchone()[0]
checkState1 = IntVar()
checkState1.set(val1)
checkBranch1 = Checkbutton(window, text='CCC Surabaya', variable=checkState1)
checkBranch1.grid(column=0, row=1)

c.execute('SELECT isChecked FROM settings where branchCode="015"')
val2 = c.fetchone()[0]
checkState2 = IntVar()
checkState2.set(val2)
checkBranch2 = Checkbutton(window, text='CCC Balikpapan', variable=checkState2)
checkBranch2.grid(column=0, row=2)

c.execute('SELECT isChecked FROM settings where branchCode="051"')
val3 = c.fetchone()[0]
checkState3 = IntVar()
checkState3.set(val3)
checkBranch3 = Checkbutton(window, text='CC', variable=checkState3)
checkBranch3.grid(column=0, row=3)

c.execute('SELECT isChecked FROM settings where branchCode="052"')
val4 = c.fetchone()[0]
checkState4 = IntVar()
checkState4.set(val4)
checkBranch4 = Checkbutton(window, text='CCC 2', variable=checkState4)
checkBranch4.grid(column=0, row=4)

c.execute('SELECT isChecked FROM settings where branchCode="054"')
val5 = c.fetchone()[0]
checkState5 = IntVar()
checkState5.set(val5)
checkBranch5 = Checkbutton(window, text='CCC 1', variable=checkState5)
checkBranch5.grid(column=0, row=5)

c.execute('SELECT isChecked FROM settings where branchCode="055"')
val6 = c.fetchone()[0]
checkState6 = IntVar()
checkState6.set(val6)
checkBranch6 = Checkbutton(window, text='Global Corporate', variable=checkState6)
checkBranch6.grid(column=0, row=6)

c.execute('SELECT isChecked FROM settings where branchCode="057"')
val7 = c.fetchone()[0]
checkState7 = IntVar()
checkState7.set(val7)
checkBranch7 = Checkbutton(window, text='CCC Makassar', variable=checkState7)
checkBranch7.grid(column=0, row=7)

c.execute('SELECT isChecked FROM settings where branchCode="300"')
val8 = c.fetchone()[0]
checkState8 = IntVar()
checkState8.set(val8)
checkBranch8 = Checkbutton(window, text='Implant', variable=checkState8)
checkBranch8.grid(column=0, row=8)

timeLabel = Label(window, text="Time Schedule (in minutes)")
timeLabel.grid(column=1, row=0)


c.execute('SELECT timeSet FROM time where id=1')
tVal = c.fetchone()[0]

textVal = StringVar()
text = Entry(window, width=10, textvariable=textVal)
text.grid(column=1, row=1)
textVal.set(tVal)


def save():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    #1
    if checkState1.get() == 1:
        query1 = 'update settings set isChecked="1" where branchCode="013"'
        c.execute(query1)
        conn.commit()
    else:
        query1 = 'update settings set isChecked="0" where branchCode="013"'
        c.execute(query1)
        conn.commit()

    #2
    if checkState2.get() == 1:
        query2 = 'update settings set isChecked="1" where branchCode="015"'
        c.execute(query2)
        conn.commit()
    else:
        query2 = 'update settings set isChecked="0" where branchCode="015"'
        c.execute(query2)
        conn.commit()

    #3
    if checkState3.get() == 1:
        query3 = 'update settings set isChecked="1" where branchCode="051"'
        c.execute(query3)
        conn.commit()
    else:
        query3 = 'update settings set isChecked="0" where branchCode="051"'
        c.execute(query3)
        conn.commit()

    #4
    if checkState4.get() == 1:
        query4 = 'update settings set isChecked="1" where branchCode="052"'
        c.execute(query4)
        conn.commit()
    else:
        query4 = 'update settings set isChecked="0" where branchCode="052"'
        c.execute(query4)
        conn.commit()

    #5
    if checkState5.get() == 1:
        query5 = 'update settings set isChecked="1" where branchCode="054"'
        c.execute(query5)
        conn.commit()
    else:
        query5 = 'update settings set isChecked="0" where branchCode="054"'
        c.execute(query5)
        conn.commit()

    #6
    if checkState6.get() == 1:
        query6 = 'update settings set isChecked="1" where branchCode="055"'
        c.execute(query6)
        conn.commit()
    else:
        query6 = 'update settings set isChecked="0" where branchCode="055"'
        c.execute(query6)
        conn.commit()

    #7
    if checkState7.get() == 1:
        query7 = 'update settings set isChecked="1" where branchCode="057"'
        c.execute(query7)
        conn.commit()
    else:
        query7 = 'update settings set isChecked="0" where branchCode="057"'
        c.execute(query7)
        conn.commit()

    #8
    if checkState8.get() == 1:
        query8 = 'update settings set isChecked="1" where branchCode="300"'
        c.execute(query8)
        conn.commit()
    else:
        query8 = 'update settings set isChecked="0" where branchCode="300"'
        c.execute(query8)
        conn.commit()

    # print(text.get())
    t = text.get()
    query9 = 'update time set timeSet=%s'%(t)
    c.execute(query9)
    conn.commit()

    conn.close()
    messagebox.showinfo('Info', 'Save Success!')

button = Button(window, text="Save", command=save)
button.grid(column=1, row=3)

window.mainloop()