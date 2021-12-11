#remove special PMIDs and their evidences
inputList = []
trimmedInputList = []
PMIDList = []
trimmedPMIDList = []

with open("input.txt","r", encoding="UTF-8") as reader:
    for i in reader.readlines():
        inputList.append(i)

for j in inputList:
    remove = j.replace("\n","")
    trimmedInputList.append(remove) #contains main file

with open("rPMID.txt", "r") as editor:
    for k in editor.readlines():
        PMIDList.append(k)

for l in PMIDList:
    remove1 = l.replace("\n","")
    trimmedPMIDList.append(remove1)  #contains removal items

def fun(m):
    index = trimmedInputList.index(m)
    if index > 0:
        del trimmedInputList[index : index+2] #delete cosecutive element
        fun(m)
        
for m in trimmedPMIDList:
    try:
        fun(m)   
    except ValueError:
        pass

with open("output.txt","w", encoding="UTF-8") as writer:
    for o in trimmedInputList:
        writer.write(o)
        writer.write("\n")


            
    





        

