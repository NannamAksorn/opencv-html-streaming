from flask import Flask, render_template, Response
import redis 
import base64 

app = Flask(__name__)

def gen():   
    r = redis.StrictRedis(host='0.0.0.0', port=6379, db=0, password='')
    while True:
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + base64.b64decode(r.get("frame")) + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
