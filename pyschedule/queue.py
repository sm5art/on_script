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

class Queue:
	def __init__(self,jobs = {}):
		self.jobs = jobs
		self.output = {}
		if platform == "linux" or platform == "linux2" or platform == "darwin":
			self.prefix = "./"
			self.suffix = ".sh"
		elif platform == "win32":
			self.prefix = ""
			self.suffix = ".bat"

	def start(self):
		for key,job in self.jobs.iteritems():
			if os.path.isfile(job):
				process = subprocess.Popen(self.prefix+job,stdout=subprocess.PIPE)
				self.output[key] = "".join(i.rstrip() + "\n" for i in process.stdout.readlines())
			else:
				name = key+self.suffix
				with open(name,"w+") as f:
					f.write(job)
				process = subprocess.Popen(self.prefix+name,stdout=subprocess.PIPE)
				self.output[key] = "".join(i.rstrip() + "\n" for i in process.stdout.readlines())
				os.remove(name)


				
				


