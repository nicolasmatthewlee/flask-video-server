from flask import Flask, Response, request
import cv2
from picamera2 import Picamera2
import time

# 1. initialize Flask app
app = Flask(__name__)

# 2. initialize the camera
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (1280, 720)})
picam2.configure(camera_config)
lens_position=10
picam2.set_controls({"AfMode":0,"LensPosition":lens_position})
picam2.start()

def gen_frames():
    while True:
        # Capture frame from picamera2
        frame = picam2.capture_array()

        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Yield frame as a byte stream for Flask to push to the client
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/settings',methods=['POST'])
def post_settings():
	'''must send integer parameter lens_position'''
	data = request.get_json()
	try:
		lens_position = data['lens_position']
		picam2.set_controls({"AfMode":0,"LensPosition":lens_position})
		return "",200
	except BaseException:
		return "",500

@app.route('/')
def index():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    # Run the Flask app on all available IP addresses (host=0.0.0.0)
    app.run(host='0.0.0.0', port=5000, debug=False)
