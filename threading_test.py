import threading
import time


def count_to_three():
    print(0)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(3)


for i in range(10):
    t = threading.Thread(target=count_to_three)
    t.start()
