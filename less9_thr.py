import threading
import time


def run1(interval):
    i = 10
    while i > 0:
        print(f'Time: {time.ctime()} Thread: {t.getName()}', i)
        time.sleep(interval)
        i = i - 1


def run2(interval):
    i = 10
    while i > 0:
        print(f'Time: {time.ctime()} Thread: {t2.getName()}', i)
        time.sleep(interval)
        i = i - 1


t = threading.Thread(target=run1, args=(1,))
t.daemon = True
t.start()
t2 = threading.Thread(target=run2, args=(1,))
t2.daemon = True
t2.start()
t.join()
t2.join()
