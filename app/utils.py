from flask import jsonify
import uuid

def handle_error(message, status_code):
    error_response = {
        'error': message,
        'status_code': status_code
    }
    return jsonify(error_response), status_code

def create_unique_uuid():
    return uuid.uuid4()