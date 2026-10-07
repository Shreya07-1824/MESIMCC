s=input("enter the string")
vowel="aeiouAEIOU"
digit="1234567890"
specialchar="@#$%^&*"
vowelcount=0
countconsonant=0
digitcount=0
specialcharcount=0


for i in vowel:
    for j in s:
        
        if(i==j):
          vowelcount+=1
       
for i in digit:
   for j in s:
      if i in j:
         digitcount+=1

for i in specialchar:
   for j in s:
      if i in j:
         specialcharcount+=1

for i in s:
   if i.isalpha() and i not in vowel:
      countconsonant+=1



print(f"vowel:{vowelcount}")
print(f"consonant:{countconsonant}")
print(f"digit:{digitcount}")
print(f"specialchar:{specialcharcount}")
        
        

            
         