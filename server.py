#!/usr/bin/env python
import eventlet
import sys
import json
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def new_assigns(*args, **kwargs):
    # Mock function that receives the message emited by the client upon
    # request completion.
    if args:
        print(args)
    if kwargs:
        print(kwargs)

@sio.event
def connect(sid, environ):
    # Upon connection of a client to this socketIO server
    # the server emits the json payload that is given to
    # this app (./server.py [json filename])
    print('Client connected: ', sid)
    print('Deliverying payload')
    with open(sys.argv[1], "r") as foo:
        payload = json.load(foo)
    sio.emit("get_assigns", payload)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./server.py [json filename]")
        sys.exit(0)

    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

