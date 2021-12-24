import time
import multiprocessing


def fun1(): # for example your potentiometer
    for i in range(5):
        time.sleep(1)


def fun2(): # for example your force sensor
    for i in range(5):
        time.sleep(1)


def normal_run():
    tic = time.time()
    fun1()
    fun2()
    toc = time.time()
    print('total time = ', toc - tic)


def multi_process_run():
    tic = time.time()
    process1 = multiprocessing.Process(target=fun1)
    process2 = multiprocessing.Process(target=fun2)
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    toc = time.time()
    print('total time = ', toc - tic)


if __name__ == '__main__': # alternate to see the effect
    # normal_run()
    multi_process_run()