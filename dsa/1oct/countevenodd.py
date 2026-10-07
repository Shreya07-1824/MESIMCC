a=int(input("enter the size of array"))
arr=[]
for i in range(a):
    b=int(input("enter the element"))
    arr.append(b)

evencount=0
oddcount=0
for i in range(0,len(arr)):
     if(arr[i]%2==0):
          evencount+=1
     else:
          oddcount+=1

print(f"even count is {evencount}")
print(f"odd count is {oddcount}")          
          
     
    