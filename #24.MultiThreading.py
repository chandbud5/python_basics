from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()        #Objects created
t2 = Hi()

t1.start()      # It will create 2 different threads
sleep(0.2) # This will make sure 2 threads do not overlap each other
t2.start()

t1.join()    #  Main thread is going to print bye bu due to join statement
t2.join()    # main thread will wait for both t1 and t2 to complete their execution then only it print bye

print("BYE") #  Executed by main thread