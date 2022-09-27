from flask import Flask, render_template, Response

import camera
from camera import Video, choice, total_headgears

app=Flask(__name__)

#rendering the HTML page which has the button
#@app.route('/index')
#def json():
 #   return render_template('json.html')

#background process happening without any refreshing

camera.choice = 0

@app.route('/')
def index():
    #global ch
    return render_template('index.html')

@app.route('/background_process_test')
def background_process_test():
    camera.choice = (camera.choice+1) % camera.total_headgears
    #global ch
    #ch = (ch + 1) % camera.total_headgears
    return ("nothing")


def gen(camera):
    #choice = 1
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@app.route('/video')

def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(debug=True)