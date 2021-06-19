from tkinter import *
root = Tk()

root.title("ASCII value")
root.geometry("400x400")

root.configure(background = "#fce303")

enter_word = Entry(root,bg="cyan")
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root,text="ASCII value",bg="#fff",fg="#000")
label.place(relx=0.5,rely=0.6,anchor=CENTER)

def asciiConv():
    word = enter_word.get()
    for letter in word:
        label['text'] += str(ord(letter)) + " "
        
        
button = Button(root,text="Convert ascii value",command=asciiConv,bg="#fff",fg="#000")
button.place(relx=0.5,rely=0.8,anchor=CENTER)    


root.mainloop()