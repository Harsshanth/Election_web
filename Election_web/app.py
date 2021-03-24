
from flask import Flask, render_template, Response, send_from_directory, stream_with_context, json
from camera import camera_stream

app = Flask(__name__)

faces_num = 0

@app.route('/face.xml')
def xml():
    return send_from_directory('static', 'haarcascade_frontalface_dataset.xml')

@app.route('/js/<path:file>')
def jsRoute(file):
    return send_from_directory('js', file)


@app.route('/css/<path:file>')
def cssRoute(file):
    return send_from_directory('css', file)


@app.route('/img/<path:file>')
def imgRoute(file):
    return send_from_directory('img', file)



@app.route('/vote')
def index():
    """Video streaming home page."""
    return render_template('vote.html')

@app.route('/final')
def finalRoute():
    """Video streaming home page."""
    return render_template('final.html')

@app.route('/timeElapsed')
def timeElalpsedRoute():
    """Video streaming home page."""
    return render_template('timeElapsed.html')

@app.route('/')
def loginRoute():
    return render_template('index.html')

@app.route('/user')
def userRoute():
    return render_template('user.html')



def gen_frame():
    global faces_num
    """Video streaming generator function."""
    while True:
        frame, num = camera_stream()
        faces_num = num
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') # concate frame one by one and show result


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/count')
def count():
    return Response(json.dumps({"count": faces_num}), mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)




