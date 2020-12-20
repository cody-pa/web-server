from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName="localhost"
serverPort=8080

class WebServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def do_GET(self):
        self._set_response()
        self.wfile.write(bytes(
        """
        <html>
            <head>
                <title>I'm Stuff</title>
            </head>
            <body>
                <form method="post">
                    <label for="user_message">Message Box</label>
                    <input type="text" id="user_message" name="user_message">
                    <input type="submit" value="Submit">
                </form> 
            </body>
        </html>
        """, "utf-8"))

    def do_POST(self):
        print("Post received.")
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        print(post_body)
        self._set_response()
        self.wfile.write("You said: {}".format(post_body).encode('utf-8'))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), WebServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")