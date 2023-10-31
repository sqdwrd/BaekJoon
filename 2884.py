hm = input().split(" ")

h = int(hm[0])
m = int(hm[1])

alH = h
alM = m - 45
if alM < 0:
    alM = 60 + alM
    alH -= 1

if alH < 0:
    alH = 23

print(alH , alM)