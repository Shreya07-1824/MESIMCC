a=int(input("enter the size of array"))
arr=[]
for i in range(a):
    b=int(input("enter the element"))
    arr.append(b)

largest=arr[0]
secondlargest=arr[0]
smallest=arr[0]
secondsmallest=arr[0]

for j in arr:
        if(j>largest):
              secondlargest=largest
              largest=j
        if(j<smallest):
             secondsmallest=smallest
             smallest=j
        elif(j<secondsmallest):
             secondsmallest=j
print(largest)
print(secondlargest)
print(smallest)
print(secondsmallest)
              
              
