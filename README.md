# socketio-server
Minimal socketio python server app. The server app receives a json filename as argument,
it set ups a socketIO server app on http://0.0.0.0:5000. The server emits this payload 
on the *get_assigns* channel to any connecting client. The given client app acknowledges
the received payload and emmits a success message into the *new_assigns* channels, 
proceeding afterwards to disconnect. The server app listens the *new_assigns* channel 
and prints the received ack.

## Instalation
```bash
pip install -r requirements
```

## Usage

On server console:
```bash
./server.py [json filename]
```

On client console:
```bash
./client.py
```
