# This is the old way of putting things into HTML with Python

import socketserver # allow python to listen to ports, and get rests from the web/elsewhere
import http.server # allows python to serve HTTP requests
import urllib.parse #manipulate URLS and query Strings

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path

        if path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers( )

            self.wfile.write(b'<html><body><h1>About Page</h1><p>This is the about page.</p></body></html>')
        else:
            self.send_error(404)

if __name__ == "__main__":
    server_address = ('localhost',8080) # the server's address will be localthost: 8080
    httpd = socketserver.TCPServer(server_address, MyHandler)

    httpd.serve_forever()
