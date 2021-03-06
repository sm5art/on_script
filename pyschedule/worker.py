import sys
import os
import threading
import queue

class Worker(threading.Thread):
    def __init__(self,jobs = {}):
        super(Worker, self).__init__()
        self.jobs = jobs
        self.output = {}
        self.start()
        self.join()
                        
    def run(self):
        executing = queue.Queue(self.jobs)
        executing.start()
        self.output = dict(executing.output)

                