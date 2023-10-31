# https://www.acmicpc.net/problem/4673
def d(n: int) -> int:
    result = n
    for i in str(n):
        result = result + int(i)
    
    return result


result = list()
for i in range(10000):
    result.append(True) #셀프 넘버이면 True


for i in range(10000):
    try:
        result[d(i)] = False
    except IndexError:
        pass


for n, i in enumerate(result):
    if i:
        print(n)
