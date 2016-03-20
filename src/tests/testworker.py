import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from worker import Worker

w1 = Worker(["echo wow","echo dank"])

print w1.execute




	
