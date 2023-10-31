global mem
mem = dict()

def search(a, b):
    if (a == 0): return b
    if (b == 1): return 1

    try:
        return mem[a][b]
    except KeyError:
        result =  search(a - 1, b) + search(a, b - 1)
        try:
            mem[a][b] = result
        except KeyError:
            mem[a] = {}
            mem[a][b] = result
        return result

T = int(input())

for i in range(T):
    a = int(input())
    b = int(input())
    
    print(search(a, b))