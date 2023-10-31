_dices = input().split(" ")
dices = []
eyeCount = [0, 0, 0, 0, 0, 0]

for i in _dices:
    dices.append(int(i))

for i in dices:
    eyeCount[i - 1] += 1

prize = None

for n, i in enumerate(eyeCount):
    if (i == 3):
        prize = (10000 + (n + 1) * 1000)
        break
    elif (i == 2):
        prize = (1000 + (n + 1) * 100)
        break
    elif (i == 1):
        prize = ((n + 1) * 100)

print(prize)