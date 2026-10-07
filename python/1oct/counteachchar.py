s=input("enter the string")
vowel="aeiouAEIOU"
count=0
for i in s:
    count=0  
    for j in vowel:
      if i == j :
        count+=1
    if(count>0):
       print(i,"count is",count)