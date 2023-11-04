# https://acmicpc.net/problem/9012

def main(len_queue):
    if len_queue == 0:
        return 0
    
    print("YES" if solve(input()) else "NO")

    main(len_queue - 1)

def solve(ps: str) -> bool:
    stack = []
    return next(ps, stack)

def next(part: str, stack: list[None]) -> bool:
    if len(part) == 0 and len(stack) == 0: return True
    elif len(part) == 0: return False

    if part[0] == "(":
        stack.append(None)
    elif part[0] == ")":
        if len(stack) == 0:
            return False
        else:
            stack.pop()
    return next(part[1:], stack)

if __name__ == "__main__":
    main(int(input()))
