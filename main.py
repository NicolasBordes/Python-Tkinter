import tkinter, PyPDF2 
import pyodbc
from tkinter import filedialog


root = tkinter.Tk()
root.title("PDF Text extractor")

def openfile():
    filename = filedialog.askopenfilename(
        title="Open PDF file",
        initialdir='U:\TDV',
        filetypes=[('PDF files','*.pdf')])
    filename_label.configure(text=filename)    
    ouputfile_texte.delete(1.0, tkinter.END)
    reader = PyPDF2.PdfReader(filename)
    for i in range(len(reader.pages)):
        current_tex = reader._get_page(i).extract_text()
        ouputfile_texte.insert(tkinter.END,current_tex) 

filename_label = tkinter.Label(root, text="No file selected")
ouputfile_texte = tkinter.Text(root)
openfile_button = tkinter.Button(root, text="open a PDF file", command=openfile)

# l'ordre est important
filename_label.pack()
ouputfile_texte.pack()
openfile_button.pack()

#création d'une table ou alors connexion auprès de cette table si elle existe déjà

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=Z:\compta\essai1.accdb;')
cursor = conn.cursor()
cursor.execute('select * from Pieces')
   
for row in cursor.fetchall():
    ouputfile_texte.insert(tkinter.END,row)

conn.close

root.mainloop()
