list=[10,10,20,30,40,40]
newlist=[]
for i in list:
    if i not in newlist:
        newlist.append(i) 
print(newlist)