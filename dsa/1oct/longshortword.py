a=input("enter string")
arr=a.split()

longest_word=arr[0]
smallest_word=arr[0]
for i in arr:
    if len(i)>len(longest_word):
        longest_word=i
    if len(i)<len(smallest_word):
        smallest_word=i
   
print("longest word is:",longest_word)
print("smallest word is:",smallest_word)



             