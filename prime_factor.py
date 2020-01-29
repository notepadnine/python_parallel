import time
import threading
import random
from multiprocessing import Process

def prime_factor(n):
    d, pf = 2, []
    while d*d <= n:
        while n %d == 0:
            pf.append(d)
            n = n // d
        d += 1
    if n > 1:
        pf.append(n)
    return pf

# split workloat in 10_000 batch
def exec_proc():
    for _ in range(10000):
        rand = random.randint(20000, 1000000000)
        print(prime_factor(rand))

def main():
    procs = []
    print('Start number crunching')
    t0 = time.time()
    for _ in range(10):
        proc = Process(target=exec_proc, args=())
        procs.append(proc)
        proc.start()
        proc.join()

    print('Total execution time:{}'.format(time.time() - t0))

if __name__ == '__main__':
    main()
ths 
jf
dsfdsf
rh