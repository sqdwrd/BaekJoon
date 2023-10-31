# https://www.acmicpc.net/problem/1065
def CheckHansu(num: str):
    num = str(num)
    if len(num) == 1:
        return True
    else:
        diff = int(num[0]) - int(num[1])
        for i in range(len(num)-1):
            if (int(num[i]) - int(num[i+1])) == diff:
                pass
            else:
                return False
        return True


if __name__ == "__main__":
    max_n = input()

    dic = list()

    for i in range(1, int(max_n) + 1):
        dic.append(CheckHansu(i))

    print(dic.count(True))
