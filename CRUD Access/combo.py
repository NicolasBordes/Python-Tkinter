from tkinter import *

root = Tk()

a = [] #creates a list to store the job names in
b = {}
var = StringVar() #creates a stringvar to store the value of options

for i  in range(20): #fills list with nonsense jobs for troubleshooting
    #a.append("Job Name - (id "+str(i)+")")
    a.append("Job Name "+str(i))
    b["Job Name "+str(i)]=i*10
 
# for cle, valeur in b.items():
#         print("l'élément de clé", cle, "vaut", valeur)

listeKey = list(b.keys())
listValue = list(b.values())

myliste = [listeKey,listValue]

# print(myliste[0])
print(myliste[1])

def getIndex(valeur):
   id = myliste[0].index(valeur)
   print(myliste[1][id])

var.set("choisissez un job") #sets the default option of options


options = OptionMenu(root, var, *myliste[0]) #createa an optionmenu populated with every element of the list
#button = Button(root, text="Ok", command=lambda:print(var.get())) #prints the current value of options
button = Button(root, text="Ok", command=lambda:getIndex(var.get())) #prints the current index of the liste




options.pack()
button.pack()

root.mainloop()