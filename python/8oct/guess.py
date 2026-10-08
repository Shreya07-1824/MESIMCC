import random
a=input("guess ")
num=["rock","paper","scisors"]

guess=random.choice(num)

if(a==guess):
    print("got an reward")
else:
    print("nice try it again")

