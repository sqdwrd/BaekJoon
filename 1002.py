cases = int(input())

for i in range(cases):
    raw = input().split(" ")
    x1 = y2 = r1 = x2 = y2 = r2 = 0
    x1 = int(raw[0])
    y1 = int(raw[1])
    r1 = int(raw[2])
    x2 = int(raw[3])
    y2 = int(raw[4])
    r2 = int(raw[5])

    if (x1 == x2 and y1 == y2 and r1 == r2):
        print("-1")
        continue

    distsq = (x1 - x2) ** 2 + (y1 - y2) ** 2
    rsq = (r1 + r2) ** 2
    rdifsq = (r1 - r2) ** 2

    if (distsq == rsq):
        print("1")    # 외접
    elif (distsq == rdifsq):
        print("1")    # 내접
    elif (rdifsq < distsq < rsq):
        print("2")    # 두 점
    else:
        print("0")
