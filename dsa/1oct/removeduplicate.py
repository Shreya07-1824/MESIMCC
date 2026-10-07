a=int(input("enter the size of array"))
arr=[]
newarr=[]
for i in range(a):
    b=int(input("enter the element"))
    arr.append(b)
for i in arr:
    if i not in newarr:
        newarr.append(i)
print(newarr)

