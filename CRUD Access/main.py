import tkinter as tk
from tkinter import ttk
import pyodbc
from random import choice
x = 0
    

#window
window = tk.Tk()
window.geometry('600x400')
window.title("Treeview")

#title of in the window
filename_label = tk.Label(window, text="table training")
filename_label.pack()

#data
firts_name = ['Bob','Maria','Alex','Charlie','Bidule','Ernestine','Justine']
last_name = ['Smith','Brown','William','Dujardin','Durant','Dupont','Cook']

#treeview
table=ttk.Treeview(window, columns=('first','last','email'),show='headings')
table.heading('first',text = 'first name')
table.heading('last',text = 'last name')
table.heading('email',text = 'email')
table.pack()

#insert values into table

for i in range(100):
    first = choice(firts_name)
    last = choice(last_name)
    email = first[0] + '.'+last +'@gmail.com'
    data = (first,last,email)
    table.insert(parent="",index=0,values=data)

listeBtn=['bnt1','btn2','btn3']
# for item in listeBtn:
#     #print(item)
#     item = tk.Button(window,text=item)
#     item.pack()
def btnAction(item):  
    global x
    #print(item.config('text')[-1])
    print(item)
    x = x + 1

def displayButton(listButton):
    
    for item in listButton:
        #print(item)
        item = tk.Button(window,text=item, command= lambda : btnAction(listButton[x]))
        item.config(width=20, height=2)
        item.pack()
        
    
displayButton(listeBtn)

#btn = tk.Button(window,text="essai de bouton", command=btnAction('essai'))

#btn.pack()

window.mainloop()




















#création d'une table ou alors connexion auprès de cette table si elle existe déjà
# au TDV, sur le serveur
#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=Z:\compta\essai1.accdb;') 
# en local, sur ce PC
# conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\n.bordes.TDV\Desktop\newPython\Tkinter\CRUD Access\essai1.accdb;')


# cursor = conn.cursor()
# cursor.execute('select * from Pieces')
# for row in cursor.fetchall():
#    print(row)

# conn.close