def chess(m, n):
    for i in range(m):
        for j in range(n):
            if (i+j) % 2 == 0:
                print("*", end=" ")
            else:
                print("#", end=" ")
        print()
chess(5 , 10)