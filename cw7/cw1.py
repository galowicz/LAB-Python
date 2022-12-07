#!/usr/bin/env python3
import sys
import numpy as np
from matplotlib import pyplot as plt, animation
import threading
import psutil
import time
from queue import Queue

queue = Queue()


def get_usage():
    while True:
        if queue.empty():
            queue.put(psutil.cpu_percent(percpu=True))
        time.sleep(0.1)


def histogram():
    fig = plt.figure()
    bins = [i for i in range(psutil.cpu_count())]
    bars = plt.bar(bins, 100, facecolor='blue')

    def animate(frame):
        tmp = queue.get()
        for cpu in range(psutil.cpu_count()):
            bars[cpu].set_height(tmp[cpu])

    ani = animation.FuncAnimation(fig, animate, frames=psutil.cpu_percent(percpu=True))
    plt.show()

if __name__ == '__main__':
    queue.put(psutil.cpu_percent(percpu=True))
    t1=threading.Thread(target=get_usage)
    t2=threading.Thread(target=histogram)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("END")
