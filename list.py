from tkinter import *
screen=Tk()
screen.geometry("500x500")
screen.title("list box")

f=Frame(screen)
f.pack()
s=Scrollbar(f)
s.pack(side=RIGHT,fill="both")

snacks=["lays","pringles","sour patch kids","dairy milk","popcorn","galaxy bar","mars","marshmallow","snickers","maggi","peanuts","corn","hakka noodles","pasta"]
welcome=Listbox(f,width=15,height=10,activestyle="dotbox",font="ariel 20 bold",yscrollcommand=s.set)
welcome.insert(1,"nachos")
for i in snacks:
    welcome.insert(1,i)
s.config(command=welcome.yview)
welcome.pack()


screen.mainloop()