# ch3/example1.py
import sys
sys.path.append("'C:\\Users\\tnguy\\PycharmProjects\\MasteringConcurrency\\Chapter03\\my_thread.py")

from my_thread import MyThread

thread1 = MyThread('A', 0.5)
thread2 = MyThread('B', 0.5)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


print('Finished.')
