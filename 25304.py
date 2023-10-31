X = int(input())
N = int(input())

sum = 0

for i in range(N):
    ab = input().split()
    sum += int(ab[0]) * int(ab[1])

print("Yes" if sum == X else "No")