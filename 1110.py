def oper(n: int):
    global depth
    global N
    new = (n % 10) * 10 + (n % 10 + n // 10) % 10
    if (N == new): return new
    depth += 1
    return oper(new)

global depth
global N

if (__name__ == "__main__"):
    depth = 1
    N = 0
    N = int(input())
    oper(N)
    print(depth)
