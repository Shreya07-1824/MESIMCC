num=1640
temp=num
pov=len(str(num))
arm=0
while(num>0):
    # r=num%10
    arm=arm+(num%10)**pov
    num=num//10

if(temp==arm):
    print("number is armstrong")
else:
    print("not armstrong")
