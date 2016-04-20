import tornado.websocket
import tornado.web
import tornado.ioloop
import os
import sys
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import pyschedule.worker as worker
from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.documents

DIR = "../stored_scripts/"



class SocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        init(self)
        print "opened"

    def on_message(self, message):
        pkg = {}
        output = {message:db.output.find_one({"name":message})["output"]}
        pkg['header']="output"
        pkg['output']=output
        self.write_message(json.dumps(pkg))

    def on_close(self):
        print "closed"

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	self.render("index.html",uri = "ws://"+self.request.host+self.request.uri+"socket")


def make_server():
	return tornado.web.Application([(r"/",MainHandler),
		(r"/socket",SocketHandler)],
		debug=True,
		template_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), "templates"),
		static_path= os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
		)

def main():
	server = make_server()
	server.listen(80)
	tornado.ioloop.IOLoop.current().start()

	
def init(soc):
	pkg = {}
	db.output.drop()
	pkg["header"] = "populate"
	for filename in os.listdir(DIR):
		
		w1 = worker.Worker(jobs={filename:filename})
		document = {
			"name":filename,
			"output":w1.output[filename],
			"date":datetime.datetime.utcnow()
			}
		pkg[filename]={
		    "src":[i.strip("\n") for i in open(os.path.abspath(os.path.join(DIR,filename))).readlines()]
		    }
		print pkg
		db.output.insert(document,check_keys=False)
		
			
	soc.write_message(json.dumps(pkg))


