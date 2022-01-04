import time
import multiprocessing
import numpy as np


def fun1(i, final_list1): # for example your potentiometer
    c = 10
    for i in range(20):
        final_list1.append(c)
        c = c + 1
        # time.sleep(1)


def fun2(i, final_list2): # for example your force sensor
    c = -10
    for i in range(20):
        final_list2.append(c)
        c = c + 1
        # time.sleep(1)


def normal_run():
    tic = time.time()
    fun1()
    fun2()
    toc = time.time()
    print('total time = ', toc - tic)


def multi_process_run():
    manager = multiprocessing.Manager()
    final_list1 = manager.list()
    final_list2 = manager.list()
    i = 0
    tic = time.time()
    process1 = multiprocessing.Process(target=fun1, args=(i, final_list1))
    process2 = multiprocessing.Process(target=fun2, args=(i, final_list2))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    toc = time.time()
    print('total time = ', toc - tic)
    r = np.zeros([20, 2])
    f1 = np.array(final_list1)
    f2 = np.array(final_list2)
    # print(f1)
    r[:, 0] = f1
    r[:, 1] = f2
    print(r)


if __name__ == '__main__': # alternate to see the effect
    # normal_run()
    multi_process_run()