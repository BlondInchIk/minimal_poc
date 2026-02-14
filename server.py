from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Примитивная имитация обработки path traversal-пути
        if "/etc/passwd" in self.path:
            fake_passwd = (
                "root:x:0:0:root:/root:/bin/bash\n"
                "www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\n"
            )
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(fake_passwd.encode())
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(
                b"Test server is running. This is a safe demo.\n"
            )


def run():
    server_address = ("0.0.0.0", 8000)
    httpd = HTTPServer(server_address, Handler)
    print("[i] Demo web server listening on 0.0.0.0:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
