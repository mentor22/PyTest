import threading #from threading import *
import time

class Hello(threading.Thread): #inherit Thread class of threading package 
    def run(self): #predefined function of thread class in threading package, for other functions start would not work
        for i in range(50):
            print("Hello")
            time.sleep(0.5) #sleep function to slow execution rate of this run() function

class Hi(threading.Thread): #inherit Thread class of threading package
    def run(self): #predefined function of thread class in threading package, for other functions start would not work
        for i in range(50):
            print("Hi")
            time.sleep(0.5) #sleep function to slow execution rate of this run() function

t1=Hello()
t2=Hi()

""" t1.run() #won't get required output as we want, it wont work simultaneously like a thread
t2.run() """
#we need to start a thread process to do something simultaneously
#but this alone still wont give required output as after waking up from sleep maybe both of them are colliding 
#both may reach to cpu for execution at same time or one may run 2-3 times until next wakes and current goes to sleep
#so we need to put sleep in between both(t1,t2) start method calls
t1.start() #first time main thread will execute it 
time.sleep(0.2) #preferable to use this time less than sleep time in run functions, same time of sleep not advised
t2.start() #after main thread executes it we can print something else too, let's try
#but that should come after all threads have ended otherwise we wont get the desired output.
#BUt "Bye" will come after first "Hello\nHi", This is because main thread will be free for 1 sec 
#It may take 1 sec for previous threads to wake up and until then main thread will execute "Bye"
#To avoid this behaviour we can use join funtions to let the threads join first(or end their part first)
t1.join()
t2.join()
print("Bye")