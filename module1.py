from tkinter import * 
k=0
def vajutatud():
    global k
    k+=1
    pealkiri.config(text=f"Sa vajutasid nuppu! {k} korda!", bg="brown")
    nupp.config(text="Vajuta veel kord!", bg="lightgray", fg="brown")
    aken.config(bg="khaki")

def valjuttudPK(event):
    global k
    k-=1
    pealkiri.config(text=f"Sa vajutasid nuppu! {k} korda!", bg="purple")
    nupp.config(text="Vajuta veel kord!", bg="black", fg="brown")
    aken.config(bg="khaki")

def tuhista(event):
    sisetus.delete(0,END)

    #sisetus.unbind("<FocusIN>")
    #sisetus.bind("<FocusOUT>", tagasi))

aken=Tk()
aken.title("Teema 8")
aken.geometry("400x400")
aken.configure(bg="darkred")
aken.resizable(width=True, height=True)
aken.iconbitmap("cat.ico")
pealkiri=Label(aken, text="Tere, tulemast Teema 8!",bg="khaki", font=("Arial",16), fg="brown")
nupp=Button(aken, text="Vajuta mind!", bg="lightgreen", font=("Arial", 12),fg="brown", relief=RAISED, command=vajutatud) #SUNKEN, RAISED,GROOVE, and RIDGE
nupp.bind("<Button-3>",valjuttudPK )
sisetus=Entry(aken, bg="white", font=("Arial", 12), fg="black")
sisetus.insert(0, "Sisesta midagi siia") #END
sisetus.bind("<FocusIN>", tuhista)
pealkiri.pack(pady=20)
nupp.pack(pady=20)
aken.mainloop()
