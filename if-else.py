from tkinter import*
def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    if(e.get()=='hi'):
        text.insert(END, "\n" + "Bot: hello")
    elif(e.get()=='hello'):
        text.insert(END, "\n" + "Bot: hi")
    elif (e.get() == 'how are you'):
        text.insert(END, "\n" + "Bot: i'm fine and you?")
    elif (e.get() == "i'm fine too"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    elif (e.get() == "give me college brochure"):
        text.insert(END, "\n" + "Bot: www.google.com")
    elif (e.get() == "q1"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    elif (e.get() == "q2"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    elif (e.get() == "q3"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.")
root = Tk()
root.title('G.S. Assi.')
text = Text(root,bg='light blue')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=80)
send = Button(root,text='Send',bg='blue',width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.mainloop()

