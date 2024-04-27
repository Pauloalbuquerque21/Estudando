
from tkinter import *

def inc():
    #Usamos o 4, pois o texto tem 4 elementos. ou seja 0,1,2,3. quando colocamos 4 acessamos o 4 elemento que é o 2
    n = int(rotulo.configure('text')[4])+1
    rotulo.configure(text=str(n))

b = Button(text='Incrementa', command=inc)
b.pack()
rotulo = Label(text='2')
rotulo.pack()
mainloop()
