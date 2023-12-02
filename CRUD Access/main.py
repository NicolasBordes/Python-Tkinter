import tkinter as tk
from tkinter import ttk
import pyodbc
from random import choice
from utiliy import showTable as test

#window
window = tk.Tk()
window.geometry('600x400')
window.title("Treeview")

#title of in the window
filename_label = tk.Label(window, text="table training")
filename_label.pack()

theColumns = ()

 
def clicked(btn):
    table.destroy()
    btn_text = btn.cget('text')
    displayTable(btn_text)

def displayButton(listButton):
    buttons =[]    
    for item in listButton:
        item  = tk.Button(window,text=item)
        item.config(width=20, height=2)
        buttons.append(item)
        
    for button in buttons:
        button.config(command=lambda btn=button: clicked(btn)) 
        # attention!! : command = lambda: clicked(button) >> ne fonctionnera pas >> les boutons cliqués renverront toujour btn3, 
        # soit le dernier de la liste
        button.pack()

def displayTable(tableName):
    # au TDV, sur le serveur
    #conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=Z:\compta\essai1.accdb;') 
    # en local, sur le PC du TDV
    #conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\n.bordes.TDV\Desktop\newPython\Tkinter\CRUD Access\essai1.accdb;')
    # en local sur le PC maison
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\nicolas\Desktop\excel BD\essai1.accdb;')
    cursor = conn.cursor()

    cursor.execute(f'select * from TablesName') # importe tous les noms de table de la base via la table "TablesName"
    global listeBtn
    listeBtn = []
    for row in cursor.fetchall():
        listeBtn.append(row[1])

    cursor.execute(f'select * from {tableName}')

    #treeview
    columns = [column[0] for column in cursor.description]
    theColumns = tuple(columns)
    nbColumns = len(theColumns)
    global table
    table=ttk.Treeview(window, columns=theColumns,show='headings')
    for item in theColumns:
        table.column(item,width=140,anchor="center")  
        table.heading(item,text = item)
    
    #fill table
    for row in cursor.fetchall():
        listRow = []
        for x in range(0,nbColumns) :
            listRow.append(row[x])
        tupleRow = tuple(listRow)    
        table.insert(parent="",index=0,values=tupleRow)
    
    table.pack()
    conn.close

displayTable("Salaries")
displayButton(listeBtn)
table.pack()
window.mainloop()