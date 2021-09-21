import threading
import time


class ClockThread(threading.Thread):
    def __init__(self, interval):
        super().__init__()
        self.daemon = True
        self.interval = interval

    def run(self):
        print(self.getName(), 'начал выполнение')
        i = 10
        while i > 0:
            print(self.getName(), i)
            time.sleep(self.interval)
            i = i - 1
        print(self.getName(), 'закончил выполнение')


t1 = ClockThread(1)
t2 = ClockThread(1)
t1.start()
t2.start()
t1.join()
t2.join()
