for i in range(1,4):
    for j in range(1,4-i):
       
       print(" " ,end="")
    for k in range(1,i+1):
      if(i==2):
       print("#",end=" ")
      elif(i==3):
         print("$",end=" ")
      else:
         print("*",end=" ")
    print("")
