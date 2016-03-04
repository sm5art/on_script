
import sys
import os


sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),  "..")) )

class Worker:
    def __init__(self,job = None):
        self.job = job
        self.source = None
        self.url = None
        self.parse_input()
        
    def parse_input(self):
        if isinstance(self.job,basestring):
            if os.path.isfile(self.job):
                self.url = self.job
            else:
                self.source = self.job
            
                
    
    def __str__(self):
    	if self.source is not None:
    		return "{:s} is source code\n".format(self.source)
    	else:
    		return  "{:s} is a file\n".format(self.url)

    #def start(self):

                