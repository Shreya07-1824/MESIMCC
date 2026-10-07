a=int(input("enter the size of array"))
arr=[]
for i in range(a):
    b=int(input("enter the element"))
    arr.append(b)

search=int(input("enter element to search"))

for i in range(0,len(arr)):
    if search==arr[i]:
        print("the element is present in array in position",i)
        isfound=True
        break

if not isfound:
     print("element not found")