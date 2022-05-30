
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(('', PORT),Handler)
print('Server listening at PORT: {0}'.format(PORT))

httpd.serve_forever()