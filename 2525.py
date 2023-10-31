_hm = input().split(" ")
h = int(_hm[0])
m = int(_hm[1])
target = int(input())

targeth = target // 60
targetm = target % 60

targetm = m + targetm
if (targetm >= 60):
    targetm = targetm - 60
    targeth = targeth + 1

targeth = h + targeth
if (targeth >= 24):
    targeth = targeth - 24

print(targeth, targetm)