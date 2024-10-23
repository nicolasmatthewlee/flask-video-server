# flask-video-server

## setup
_using Python3.11.2_

1. run server (opens on port 5000)
```shell
python server.py
```

2. run localtunnel
```shell
lt --port 5000
```

3. get localtunnel password by visiting [here](https://loca.lt/mytunnelpassword) from the machine running localtunnel
_the server is now accessible anywhere on the internet from the localtunnel url_

## setting the lens position

1. send POST request to `/settings`
```shell
curl -X POST http://localhost:5000/settings -H "Content-Type: application/json" -d '{"lens_position": 10}'
```
_when sending over localtunnel, just add `/settings` to the end of the localtunnel url_

## send stream to YouTube

1. in YouTube studio start a livestream from video stream

2. run the following to start the stream from the ArduCam 16MP IMX519
```shell
libcamera-vid -t 0 --width 1280 --height 720 --framerate 30 --nopreview --codec yuv420 -o - | ffmpeg -thread_queue_size 1024 -re -f rawvideo -pix_fmt yuv420p -s 1280x720 -r 30 -i - -thread_queue_size 1024 -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 -c:v libx264 -b:v 1500k -maxrate 1500k -bufsize 3000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 128k -f flv rtmp://a.rtmp.youtube.com/live2/YOUR_STREAM_KEY
```

## notes

- IMX519 is not a V4L2 device so commands with `v4l2-ctl` will not be able to access it
