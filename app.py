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
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())

            # self.wfile.write('') # you could write html manually here, but not recommended.

        elif '/styles.css':
            self.send_response(200)
            self.send_header('Content-Type', 'text/css')
            self.end_headers( )
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())

        elif path == "/about":
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers( )

            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())


        else:
            self.send_error(404)

if __name__ == "__main__":
    server_address = ('localhost',8080) # the server's address will be localthost: 8080
    httpd = socketserver.TCPServer(server_address, MyHandler)

    httpd.serve_forever()
