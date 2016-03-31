import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from pyschedule.worker import Worker

w1 = Worker({"wow":"echo wow","dank":"echo dank"})

print w1.output




	
