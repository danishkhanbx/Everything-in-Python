# Multithreading is a model of program execution that allows for multiple threads to be created
# within a process, executing independently but concurrently sharing process resources.

from threading import *
from time import sleep


class Hello(Thread):  # class Hello & Hi are inheriting class Thread
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(0.2)  # we sleep t1 so t2 can get executed then t2 will sleep after some time


class Hi(Thread):  # can only perform threading functions in a Subclass of Thread
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(0.2)  # so t1 can get executed making it a Multithreading model


# Objects of classes
t1 = Hello()
t2 = Hi()

# calling threading functions inside the object
t1.start()  # start will implicitly call run
sleep(0.2)  # we have divided the main thread into t1, t2 & main thread which will run different functions
t2.start()  # context switching will be happening between the threads to make this a Multithreading model

t1.join()  # MAIN thread -> t1, t2, & main, and now
t2.join()  # t1 + main = Main then t2 + Main = MAIN
print('Bye')  # MAIN thread will execute this after completing then merging t1 & t2 in it
