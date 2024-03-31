import coff
import tkinter as tk


wind = tk.Tk()
wind.title("Coffer machine")
wind.iconbitmap('C:/Users/soufyan/Desktop/scripts/z_python/tk_project/Iconsmind-Outline-Coffee.ico')
m_frame = tk.Frame(wind)
m_frame.pack()

def enabling(chice):
    if but1["state"]==tk.NORMAL:
        but1["state"]=tk.DISABLED
        but2["state"]=tk.NORMAL
        but5["state"]=tk.NORMAL
        but3["state"]=tk.NORMAL
        but4["state"]=tk.NORMAL
        return None
    if chice == "esp":
        but4["state"]=tk.DISABLED
        but5["state"]=tk.DISABLED
        but6["state"]=tk.NORMAL
        inp["state"]=tk.NORMAL
        coff.make_Espresso()
        tx.insert(1.0,"your order prix is 50 DA")
    elif chice == "lat":
        but5["state"]=tk.DISABLED
        but3["state"]=tk.DISABLED
        but6["state"]=tk.NORMAL
        inp["state"]=tk.NORMAL  
        coff.make_lattee()
        tx.insert(1.0,"your order prix is 40 DA")
    elif chice == "cup":
        but3["state"]=tk.DISABLED
        but4["state"]=tk.DISABLED
        but6["state"]=tk.NORMAL
        inp["state"]=tk.NORMAL 
        coff.make_cuppocino()
        tx.insert(1.0,"your order prix is 80 DA")

def disabling():
    but1["state"]=tk.NORMAL
    but2["state"]=tk.DISABLED
    but5["state"]=tk.DISABLED
    but3["state"]=tk.DISABLED
    but4["state"]=tk.DISABLED
    but6["state"]=tk.DISABLED
    inp.delete(0,"end")
    inp["state"]=tk.DISABLED
    tx.delete(1.0,"end")
    

def p():
    pay = int(inp.get())
    if but3["state"]==tk.NORMAL:
        tx.delete(1.0,"end")
        if pay < coff.es_co:
            tx.insert(1.0,"you paid less then coast\nyour order prix is 50 DA")
            return None
        tx.insert(1.0,"your give back is : {}\nhere is your drink Good day".format(coff.payment("ESPRESSO",pay)))
        wind.after(4000,disabling)
    elif but4["state"]==tk.NORMAL:
        tx.delete(1.0,"end")
        if pay < coff.lat_co:
            tx.insert(1.0,"you paid less then coast\nyour order prix is 40 DA")
            return None
        tx.insert(1.0,"your give back is : {}\nhere is your drink Good day".format(coff.payment("LATTEE",pay)))
        wind.after(4000,disabling)
    elif  but5["state"]==tk.NORMAL:
        tx.delete(1.0,"end")
        if pay < coff.cup_co:
            tx.insert(1.0,"you paid less then coast\nyour order prix is 80 DA")
            return None
        tx.insert(1.0,"your give back is : {}\nhere is your drink Good day".format(coff.payment("CUPPOCINO",pay)))
        wind.after(4000,disabling)
        
    

first_lable = tk.LabelFrame(m_frame,padx=73,pady=20)
first_lable.grid(row=0,column=0)
lab1 = tk.Label(first_lable,text="do you want to start or quit the machine:")
lab1.grid(row=0,column=0)
but1 = tk.Button(first_lable,text='start',padx=30,pady=10,command=lambda:enabling(""))
but1.grid(row=0,column=1)
but2 = tk.Button(first_lable,text='quit',padx=30,pady=10,state="disabled",command=disabling)
but2.grid(row=0,column=2)

second_lable = tk.LabelFrame(m_frame,padx=90,pady=20)
second_lable.grid(row=1,column=0)
lab2 = tk.Label(second_lable,text='chose whate you want to drink: ')
lab2.grid(row=0,column=0,columnspan=3)
but3 = tk.Button(second_lable,text='espresso',padx=30,pady=10,state='disabled',command=lambda:enabling("esp"))
but3.grid(row=1,column=0)
but4 = tk.Button(second_lable,text='lattee',padx=30,pady=10,state='disabled',command=lambda:enabling("lat"))
but4.grid(row=1,column=1)
but5 = tk.Button(second_lable,text='cuppocino',padx=30,pady=10,state='disabled',command=lambda:enabling("cup"))
but5.grid(row=1,column=2)

lab4 = tk.Label(second_lable,text="the current amounts: ")
lab4.grid(row=2,column=0,columnspan=4)
lab5 = tk.Label(second_lable,text='{}L'.format(coff.tea))
lab5.grid(row=3,column=0)
lab6 = tk.Label(second_lable,text='{}L'.format(coff.water))
lab6.grid(row=3,column=1)
lab7 = tk.Label(second_lable,text='{}L'.format(coff.milk))
lab7.grid(row=3,column=2)
lab8 = tk.Label(second_lable,text='{}L'.format(coff.coffer))
lab8.grid(row=3,column=3)

therd_lable  = tk.LabelFrame(m_frame,padx=151,pady=20)
therd_lable.grid(row=2,column=0)
lab3 = tk.Label(therd_lable,text='please pay for the coffee')
lab3.grid(row=0,column=0)
inp = tk.Entry(therd_lable,state='disabled',width=10)
inp.grid(row=0,column=1)
pay = inp.get()
but6  = tk.Button(therd_lable,text="pay",state="disabled",command=p)
but6.grid(row=0,column=2,padx=10,pady=10)
wind.bind('<Return>',lambda event:p())

mess = tk.Canvas(m_frame,height=100,width=10)
mess.grid(row=3,column=0)

tx  = tk.Text(mess,height=10,width=66,font=("rubik",10))
tx.pack()


wind.mainloop()

