import os
from flask import Flask
from app.routes import subscription_routes

# Define your shared secrets
shared_secrets = {
    'partner1': 'partner1_secret',
    'partner2': 'partner2_secret',
}

def create_app():
    app = Flask(__name__)

    # Register routes
    app.register_blueprint(subscription_routes)

    return app