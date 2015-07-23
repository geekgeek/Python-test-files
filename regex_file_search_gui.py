import re
from Tkinter import *
#blank window
root = Tk()

#create label,textboxes and checkbox
label1 = Label(root, text="dir")
label2 = Label(root, text="regex")

textbox1 = Entry(root)
textbox2 = Entry(root)

#C:\Users\test.txt
#sampleRegex: \bwordToSearchFor\b

def getTextbox1Text():
    fileLocation = textbox1.get()
    regexLocation = textbox2.get()

    names_file = open(fileLocation ,"r") # r = read, w = write
    data = names_file.read()
    regexLine = regexLocation
    line = re.findall(regexLine, data, re.X|re.M)
    print(line)

checkbox1 = Checkbutton(root, text="checbox1")

button1 = Button(root, text="call function", command=getTextbox1Text)

#Create alignments / sticky e = align to east
label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)

textbox1.grid(row=0, column=1)
textbox2.grid(row=1, column=1)
button1.grid(row=2,column=1)

root.mainloop()
