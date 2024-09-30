from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio

@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room."""
    room = session.get('room')
    join_room(room)
    emit('status', {
        'msg': f"{session.get('name')} has entered the room.",
    }, to=room)

@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message."""
    room = session.get('room')
    emit('message', {
        'msg': f"{session.get('name')}: {message['msg']}",
    }, to=room)

@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {
        'msg': f"{session.get('name')} has left the room.",
    }, to=room)
