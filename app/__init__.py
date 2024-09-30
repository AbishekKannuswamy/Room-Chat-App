from flask import Flask
from flask_socketio import SocketIO

# Initialize SocketIO
socketio = SocketIO()

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    # Register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Initialize SocketIO with CORS support
    socketio.init_app(app, cors_allowed_origins="*")  # Enable CORS for all origins

    return app
