from tkinter import*
obj1=Tk()
obj1.title('getting started with widgets')
obj1.geometry("400x300")

lbl=Label(text='product of numbers',fg='black',bg='blue')

lbl1=Label(text='enter num 1',fg='black',bg='blue',width=300)
entry1=Entry() 

lbl2=Label(text='enter num 2',fg='black',bg='blue',width=300)
entry2=Entry() 

lbl3=Label(text='the product is',fg='black',bg='blue',width=30)
a=entry1
b=entry2
def product():

    c=int(a.get())*int(b.get())
    entry3=Label(text=c)
    entry3.pack()
    



btn=Button(obj1,text='multiply',fg='white',bg='blue',command=product)

lbl.pack()
lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
btn.pack()
lbl3.pack()


obj1.mainloop()
