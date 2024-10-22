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

