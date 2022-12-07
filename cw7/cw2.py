import threading
import time


class Fork(threading.Semaphore):

    def take_semaphor(self):
        locked = self.acquire(False)
        if locked:
            return
        else:
            raise ResourceWarning


class Filozof(threading.Thread):
    def __init__(self, index, leftfork, rightfork):
        threading.Thread.__init__(self)
        self.running = True
        self.index = index
        self.leftfork = leftfork
        self.rightfork = rightfork

    def run(self):
        while self.running:
            print('%s filozof chce jeść' % self.index)
            self.take_fork()

    def take_fork(self):
        fork1, fork2 = self.leftfork, self.rightfork
        while self.running:
            try:
                fork1.take_semaphor()
            except ResourceWarning:
                continue
            else:
                try:
                    fork2.take_semaphor()
                except ResourceWarning:
                    fork1.release()
                else:
                    break

        self.eat()
        fork1.release()
        fork2.release()
        self.running = False

    def eat(self):
        print('%s filozof je' % self.index)
        time.sleep(2)
        print('%s filozof zjadł' % self.index)
    

if __name__ == '__main__':
    forks = [Fork() for _ in range(5)]
    filozofowie = [Filozof(i, forks[i % 5], forks[(i+1) % 5]) for i in range(5)]
    for n in filozofowie:
        n.start()
    time.sleep(25)
    Filozof.running = False
    print("Koniec")
