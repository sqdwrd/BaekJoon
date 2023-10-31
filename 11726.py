'''
9095 1, 2, 3 더하기랑 비슷함
'''
mem = [None for _ in range(1001)]

mem[1] = 1
mem[2] = 1 * 2

def partition(n: int):
    '''
    2 = 1+1 = 2

    3 = 2+1 = 1+2 = 1+1+1

    4 = 2+2 = 2+1+1 = 1+2+1 = 1+1+2 = 1+1+1+1
    '''
    if n == 1: return mem[1]
    if n == 2: return mem[2]
    if mem[n] is not None: return mem[n]

    mem[n] = partition(n - 1) + partition(n - 2)
    return mem[n]

if __name__ == "__main__":
    N = int(input())
    print(partition(N) % 10007)
