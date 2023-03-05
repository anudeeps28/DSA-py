from ast import arg
from http.client import BadStatusLine
import time
import multiprocessing

def deposit (balance, lock):
    for i in range (100):
        time.sleep(0.01)
        lock.acquire() #starting lock
        balance.value = balance.value + 1
        lock.release() # ending lock

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()
    
if __name__ == "__main__":
    balance = multiprocessing.Value("i", 200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args=(balance, lock))
    w = multiprocessing.Process(target=withdraw, args=(balance, lock))

    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)
