# source: https://stackoverflow.com/questions/12499171/can-i-set-a-header-with-pythons-simplehttpserver/13354482#13354482
from http import server

class MyHTTPRequestHandler(server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        # server.SimpleHTTPRequestHandler.end_headers(self)
        super(MyHTTPRequestHandler, self).end_headers()

    def send_my_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")


if __name__ == '__main__':
    server.test(HandlerClass=MyHTTPRequestHandler)