"""
Queue is a class used in worker to create a queue of 
scripts/source of scripts to run synchronously.
The list of jobs that you give are run in order from 0 to n, 
no matter the type(source/file). If you give source code
a temporary file is created for execution but will be removed upon end
of execution. Source code can only be a system script(bat/sh).
"""

import os
from sys import platform
import subprocess
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

class Queue:
	def __init__(self,jobs = []):
		self.jobs = jobs
		self.execute = {}
		if platform == "linux" or platform == "linux2" or platform == "darwin":
			self.prefix = "./"
			self.suffix = ".sh"
		elif platform == "win32":
			self.prefix = ""
			self.suffix = ".bat"

	def start(self):
		for i,job in enumerate(self.jobs):
			if os.path.isfile(job):
				process = subprocess.Popen(self.prefix+name,stdout=subprocess.PIPE)
				self.execute[job] = process.stdout.readlines()
			else:
				name = "temp"+str(i)+self.suffix
				with open(name,"w+") as f:
					f.write(job)
				process = subprocess.Popen(self.prefix+name,stdout=subprocess.PIPE)
				self.execute[name] = process.stdout.readlines()
				os.remove(name)


				
				


