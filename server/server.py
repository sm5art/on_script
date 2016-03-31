import tornado.websocket
import tornado.web
import tornado.ioloop
import os
import json


bradberry = {}
class SocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        self.write_message(json.dumps(bradberry))

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

def main(worker=None):
	global bradberry
	bradberry = dict(worker.output)
	server = make_server()
	server.listen(8888)
	tornado.ioloop.IOLoop.current().start()
	
