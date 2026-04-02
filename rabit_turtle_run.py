import multiprocessing
import time
import random

# 函数式编程实现一个龟兔赛跑的案例

finish = 10

def turtle_run():
    # 乌龟跑步的时候会发生什么
    pos = 0 # 首先起点为0
    # 什么情况下乌龟才会跑
    while pos < finish:
        pos += 1
        print('乌龟跑了一米')
        time.sleep(1)
        print('乌龟休息一秒钟')
    print("乌龟到达终点")

def rabit_run():
    pos = 0
    while pos < finish:
        pos += 2
        print('兔子跑了两米')
        time.sleep(random.randint(1,10))
        print('兔子休息了一会')
    print("兔子到达终点")

if __name__ == '__main__':
    print("🚩 龟兔赛跑开始！")

    # 创建两个进程
    t1 = multiprocessing.Process(target=turtle_run)
    t2 = multiprocessing.Process(target=rabit_run)

    # 启动
    t1.start()
    t2.start()

    # 等待结束
    t1.join()
    t2.join()

    print("🏁 比赛结束！")



