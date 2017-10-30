import urllib.request
import random
import threading
from multiprocessing import Process
import time


def download_image(image_path, file_name):
    print("Downloading image from ", image_path)
    urllib.request.urlretrieve(image_path, file_name)


def execute_thread(i):
    image_name = "images/image-{}.jpg".format(i)
    download_image("http://lorempixel.com/400/200/sports/", image_name)


def main():
    t0 = time.time()
    threads = []
    for i in range(10):
        thread = threading.Thread(target=execute_thread, args=(i,))
        threads.append(thread)
        thread.start()
    [thread.join() for thread in threads]
    t1 = time.time()
    total_time = t1 - t0
    print("Total execution time {}".format(total_time))


def calculate_prime_factors(n):
    prime_factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            prime_factors.append(d)
            n //= d
        d += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors

# End of first example


def main2():
    print("Starting number crunching...")
    t0 = time.time()

    for _ in range(10000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime_factors(rand))

    t1 = time.time()
    total_time = t1 - t0
    print("Execution time: {}".format(total_time))


def execute_proc():
    for _ in range(1000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime_factors(rand))


def main3():
    print("Starting number crunching...")
    t0 = time.time()
    procs = []
    for _ in range(10):
        proc = Process(target=execute_proc, args=())
        procs.append(proc)
        proc.start()
    [proc.join() for proc in procs]
    t1 = time.time()
    total_time = t1 - t0
    print("Execution time: {}".format(total_time))

if __name__ == '__main__':
    main3()
