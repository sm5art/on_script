import tornado.websocket
import tornado.web
import tornado.ioloop
import os
import json

DIR = "../stored_scripts/"

class SocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        init(self)

    def on_close(self):
        print "closed"

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	self.render("index.html")


def make_server():
	return tornado.web.Application([(r"/",MainHandler),
		(r"/socket",SocketHandler)],
		debug=True,
		template_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), "templates"),
		static_path= os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
		)

def main():
	server = make_server()
	server.listen(8888)
	tornado.ioloop.IOLoop.current().start()
	
def init(soc):
	pkg = {}
	for filename in os.listdir(DIR):
		with open(DIR+filename) as f:
			lines = f.readlines()
			pkg[filename]={"length":len(lines),"src":[i.strip("\n") for i in lines]}
	print pkg
	soc.write_message(json.dumps(pkg))


