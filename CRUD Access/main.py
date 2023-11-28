import tkinter as tk
from tkinter import ttk
import pyodbc
from random import choice

#window
window = tk.Tk()
window.geometry('600x400')
window.title("Treeview")

#title of in the window
filename_label = tk.Label(window, text="table training")
filename_label.pack()

#treeview
table=ttk.Treeview(window, columns=('Titre','MetteurEnScene','Auteur','resumer'),show='headings')
table.column("Titre",width=140,anchor="center")
table.column("MetteurEnScene",width=140,anchor="center")
table.column("Auteur",width=140,anchor="center")
table.column("resumer",width=180,anchor="center")
table.heading('Titre',text = 'Titre')
table.heading('MetteurEnScene',text = 'Metteur en scène')
table.heading('Auteur',text = 'Auteur')
table.heading('resumer',text = 'Résumer')
table.pack()

listeBtn=['Lieux','Pieces','Salaries']

def btnAction(item):  
     print(item.cget('text'))
 
def clicked(btn):
    for i in table.get_children():
        table.delete(i)
        window.update()
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

displayButton(listeBtn)

def displayTable(tableName):
    #création d'une table ou alors connexion auprès de cette table si elle existe déjà
    # au TDV, sur le serveur
    #conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=Z:\compta\essai1.accdb;') 
    # en local, sur ce PC
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\n.bordes.TDV\Desktop\newPython\Tkinter\CRUD Access\essai1.accdb;')
    cursor = conn.cursor()
    cursor.execute(f'select * from {tableName}')
    #insert values into table
    # for item in listeBtn:
    #     table.column(item,anchor="CENTER",stretch="NO",width=20)
    
    for row in cursor.fetchall():
        col1 = row[1]
        col2 = row[2]
        col3 = row[3]
        col4 = row[4]
        data = (col1,col2,col3,col4)
        table.insert(parent="",index=0,values=data)
    # pour obtenir la liste des entêtes de colonnes 
    columns = [column[0] for column in cursor.description]
    print(columns)
    conn.close

displayTable("Salaries")

window.mainloop()