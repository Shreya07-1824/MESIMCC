a=int(input("enter the size of array"))
arr=[]
for i in range(a):
    b=int(input("enter the element"))
    arr.append(b)
index=0
for i in arr:
    if i !=0:
        arr[index]=i
        index+=1

for i in range(index,len(arr)):
    arr[index]=0
    index+=1

print(arr)