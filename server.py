from http.server import HTTPServer, BaseHTTPRequestHandler
import ASUS.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            print("LED OFF")
            GPIO.output(3,GPIO.LOW)
            time.sleep(2)
            GPIO.output(3,GPIO.HIGH)
            print("LED ON")
            time.sleep(2)
            print("LED OFF")
            GPIO.output(3,GPIO.LOW)

            file_to_open = "Hello world!"
            self.send_response(200)
        except:
            print("LED OFF")
            GPIO.output(3,GPIO.LOW)
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('', 8080), Serv)
httpd.serve_forever()

GPIO.cleanup()
