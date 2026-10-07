a=int(input("enter the size of array"))
arr=[]
for i in range(a):
    b=int(input("enter the element"))
    arr.append(b)
start=0
end=len(arr)-1
for i in range(start,end):
    while(start<end):
       temp=arr[start]
       arr[start]=arr[end]
       arr[end]=temp

       start+=1
       end-=1
print(arr)