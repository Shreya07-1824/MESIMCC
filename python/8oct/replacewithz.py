s="shreya"
vowel="aeiou"
result=""
for i in s:
    if i in vowel:
        result+='z'
    else:
        result+=i

print(result)