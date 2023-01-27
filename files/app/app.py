from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return "Hostname %s requested by NGINX frontend.\n" % (socket.gethostname())

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
