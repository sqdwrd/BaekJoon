mem = [None for _ in range(11)]
mem[0] = None
mem[1] = 1
mem[2] = 2
mem[3] = 4

def solve(ns: list[int]):
    if (len(ns)) == 0:
        return
    print(partition(ns.pop(0)))
    solve(ns)

def partition(n: int):
    '''
    2를 분할하는 방법 1+1
        2는 1+1로 분할할 수도 있고 안할 수도 있고
    3을 분할하는 방법 1+1+1/1+2/2+1
        3은 1+2로 분할할 수도 있고 2+1로 분할할 수도 있고 안할 수도 있고
        2는 1+1로 분할할 수도 있고 안할 수도 있고


    n (n > 3)을 분할하는 방법
        n은 1+(n-1)로 분할할 수도 있고 2+(n-2)로 분할할 수도 있고 3+(n-3)으로 분할할 수도 있고 (안할수는 없다)
    '''
    if mem[n] is None:
        mem[n] = partition(n-1) + partition(n-2) + partition(n-3)

    return mem[n]

if __name__ == "__main__":
    T = int(input())
    Ns = [int(input()) for _ in range(T)]
    solve(Ns)