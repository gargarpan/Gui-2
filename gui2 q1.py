from tkinter import *
dict={1:'qw',2:'as',3:'asw',4:'asx',5:'cfd',6:'aqz',7:'cfd',8:'ert',9:'asdf',10:'aqwes',11:'as'}

root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=sb.set)
for line in range(13):
    mylist.insert(END, 'Hi '+str(line))
mylist.pack(side=LEFT, fill=Y)
sb.configure(command=mylist.yview)

root.mainloop()
