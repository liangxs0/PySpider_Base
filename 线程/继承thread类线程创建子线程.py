import threading
import time 

class MyThread(threading.Thread):
    def __init__(self,second):
        threading.Thread.__init__(self)
        self.second = second
    
    def run(self)