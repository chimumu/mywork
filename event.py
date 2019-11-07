import threading
import time

event = threading.Event()

def lighter():
    count = 0
    while True:
        if count < 5:  # 绿灯
            event.set()  #设置标志位
            print("\033[42;1m 绿灯亮\033[0m")
        elif count > 10:
            count =0  # 清零重新计数
        else:  # 红灯
            event.clear()  # 清空标志
            print("\033[41;1m 红灯亮\033[0m")

        time.sleep(1)
        count += 1

def chihuoguo(name):
    print('%s已经启动'%threading.current_thread().getName())
    print('小伙伴%s已经进入就餐状态'%name)
    time.sleep(1)
    event.wait()
    print('%s收到通知'%threading.current_thread().getName())
    print ('小伙伴 %s 开始吃咯！' % name)

# 设置线程组
threads = []

# 创建新线程
thread1 = threading.Thread(target=chihuoguo, args=("a",))
thread2 = threading.Thread(target=chihuoguo, args=("b",))

# 添加到线程组
threads.append(thread1)
threads.append(thread2)

# 开启线程
for thread in threads:
    thread.start()

time.sleep(0.1)
# 发送事件通知
print
'主线程通知小伙伴开吃咯！'
event.set()
