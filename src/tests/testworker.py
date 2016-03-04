
import sys
import os


sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),  "..")) )
from factory.worker import Worker

worker = Worker("print 'hello'")
worker1 = Worker("wow.txt")
print worker,worker1
	
