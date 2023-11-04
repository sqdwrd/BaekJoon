# https://acmicpc.net/problem/9012

def main(len_queue):
    if len_queue == 0:
        return 0
    
    print("YES" if solve(input()) else "NO")

    main(len_queue - 1)

def solve(ps: str) -> bool:
    stack = 0
    return next(ps, stack)

def next(part: str, stack: int) -> bool:
    if len(part) == 0 and stack == 0: return True
    elif len(part) == 0: return False

    if part[0] == "(":
        stack = stack + 1
    elif part[0] == ")":
        if stack == 0:
            return False
        else:
            stack = stack - 1
    return next(part[1:], stack)

if __name__ == "__main__":
    main(int(input()))
