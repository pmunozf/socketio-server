#!/usr/bin/env python
import socketio
import http.client
import os
import json
import sys
sio = socketio.Client()

@sio.event
def get_assigns(payload):
    print(json.dumps(payload, indent=4))
    sio.emit("new_assigns", {"msg" : "payload received", "payload" : payload})
    sio.disconnect()

if __name__ == '__main__':
    url = "http://0.0.0.0:5000"
    sio.connect(url)

