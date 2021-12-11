#remove genes with aliases
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
    lists1.append(remove) #contains main file


with open("rGenes.txt", "r") as editor:
    for k in editor.readlines():
        lists3.append(k)

for l in lists3:
    remove1 = l.replace("\n","")
    lists4.append(remove1) #contain gene symbols


for i in lists4:
        lists1 = list(map(lambda st: str.replace(st, i, ""), lists1))


                      
with open("output.txt","w", encoding="UTF-8") as writer:
    for o in lists1:
        writer.write(o)
        writer.write("\n")

