#remove official genes 
lists = []
lists1 = []
lists2 = []
lists3 = []
lists4 = []
lists5 = []

with open("input.txt", "r", encoding="UTF-8") as reader:
    for i in reader.readlines():
        lists.append(i)

for j in lists:
    remove = j.replace("\n","")
    lists1.append(remove) 

for j in lists1:
    remove1 = j.replace(">> ","")
    lists2.append(remove1) #contains main file

with open("rGenes.txt", "r") as editor:
    for k in editor.readlines():
        lists3.append(k)

for l in lists3:
    remove1 = l.replace("\n","")
    lists4.append(remove1)

for j in lists4:
    remove1 = j.capitalize()
    lists5.append(remove1)    #contains removal items
    


for i in lists5:
    try:
        lists2[lists2.index(i)] = "<<<<<<<<<<<<removed_gene>>>>>>>>>>>>>"
    except ValueError:
        pass


with open("output.txt","w", encoding="UTF-8") as writer:
    for o in lists2:
        writer.write(o)
        writer.write("\n")


            
    

#lists4 = [i for i in lists1 if i not in lists3]



        

