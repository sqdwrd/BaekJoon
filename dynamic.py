import time
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(5003)

# 메모이제이션을 사용하지 않았을 때
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n - 2)

# 메모이제이션을 사용했을 때
class dynamic:
    mem = [0, 1]


    def dynamicFib(self, n):
        if len(self.mem) - 1 < n:
            self.mem.append(self.dynamicFib(n - 2) + self.dynamicFib(n - 1))
            return self.mem[n]
        else:
            return self.mem[n]


def draw_wout_dynamic():
    start_time = time.time()
    time_list = []
    time_complexity_list = []

    plt.rc('font', family="Apple SD Gothic Neo")
    plt.show()
    for i in range(1, 40):
        step_start_time = time.time()
        fib(i)
        time_list.append(time.time() - step_start_time)
    print(f"메모이제이션을 사용하지 않았을 때: {time.time() - start_time}")
        
    plt.subplot(1, 2, 1)
    plt.xlabel("x번째 피보나치 수")
    plt.ylabel("걸린 시간(초)")

    plt.plot(time_list, color="red")
    plt.draw()

    plt.subplot(1, 2, 2)
    plt.xlabel("2^x의 개형")
    for i in range(1, 40):
        time_complexity_list.append(100*(2**(i-7)))
    plt.plot(time_complexity_list, color="grey")
    plt.pause(0.001)
    plt.savefig("without_dynamic.png")

def draw_dynamic():
    plt.figure(figsize=(8,4))
    start_time = time.time()
    time_list = []
    dynamicobj = dynamic()

    for i in range(1, 10000):
        step_start_time = time.time()
        dynamicobj.dynamicFib(i)
        time_list.append(time.time() - step_start_time)
        dynamicobj.mem = [0,1]
    print(f"메모이제이션을 사용했을 때: {time.time() - start_time}")
        
    plt.xlabel("x번째 피보나치 수")
    plt.ylabel("걸린 시간(초)")

    plt.plot(time_list, color="dodgerblue")
    plt.draw()

    plt.pause(0.001)
    plt.savefig("dynamic.png")
    plt.show()

# draw_wout_dynamic()
draw_dynamic()