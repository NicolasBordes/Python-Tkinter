from tkinter import *

root = Tk()
root.geometry("600x400")
b = {}
var = StringVar() #creates a stringvar to store the value of options

for i  in range(20): #fills list with nonsense jobs for troubleshooting
    b["Job Name "+str(i)]=i*10
 
listeKey = list(b.keys())
listValue = list(b.values())
myliste = [listeKey,listValue]
#ajout d'un commentaire test der
def getIndex(valeur):
   id = myliste[0].index(valeur)
   print(myliste[1][id])

var.set("choisissez un job") #sets the default option of options

options = OptionMenu(root, var, *myliste[0]) #createa an optionmenu populated with every element of the list
button = Button(root, text="Ok", command=lambda:getIndex(var.get())) #prints the current index of the liste


options.pack()
button.pack()

root.mainloop()