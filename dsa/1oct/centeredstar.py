for i in range(6):
    for j in range(1,6-i):
          print(" ",end="")
    for j in range(1, i+1):
        print(j, end=" ")

    # decreasing numbers
    for j in range(i-1, 0, -1):
        print(i, end=" ")

    print()
