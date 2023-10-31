# https://www.acmicpc.net/problem/1003
"""
fib(n)이 0이 되는 횟수와 fib(n)이 1이 되는 횟수 구하기
fib(0), fib(1)이 호출되는 횟수 구하기
"""

zero = [1, 0, 1]
one = [0, 1, 1]


def fib(n):
    if n > len(zero) - 1:
        for i in range(len(zero), n + 1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] +  one[i-2])
    print(f"{zero[n]} {one[n]}")


for i in range(int(input())):
    fib(int(input()))
