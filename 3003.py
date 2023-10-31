pieces = input().split(" ")

for n, i in enumerate(pieces):
    if (n == 0 or n == 1):
        print(1 - int(i), end=" ")
    elif (n == 5):
        print(8 - int(i), end=" ")
    else: 
        print(2 - int(i), end=" ")

