import os
from flask import Blueprint, request, jsonify
from app.middleware import PartnerAuthenticationMiddleware
from app.utils import handle_error
from app.database import store_subscription, store_user, get_subscription_by_user_external_id, update_subscription
from app.models import Subscription, User

# Get the shared secrets from environment variables
shared_secrets = {
    'partner1': os.getenv('PARTNER1_SECRET'),
    'partner2': os.getenv('PARTNER2_SECRET'),
}

# Create a Blueprint for routes
subscription_routes = Blueprint('subscription_routes', __name__)

# Create an instance of the authentication middleware
required_partner_authentication = PartnerAuthenticationMiddleware(subscription_routes, shared_secrets).required_authentication

@subscription_routes.route('/api/v1/subscription', methods=['POST'])
@required_partner_authentication
def create_subscription():
    try:
        # Parse request payload
        payload = request.get_json()
        external_id, user_email, duration, expiration_date = (
            payload.get('external_id'),
            payload.get('user_email'),
            payload.get('duration'),
            payload.get('expiration_date'),
        )

        # Validate request payload
        if not external_id or not user_email or not duration:
            return handle_error('Invalid payload', 400)

        # Store user and the subscription
        user = User(external_id, user_email)
        subscription = Subscription(user, duration, expiration_date)
        store_user(user)
        store_subscription(subscription)

        return jsonify({'message': 'Subscription created successfully'}), 201

    except Exception as e:
        return handle_error(str(e), 500)

@subscription_routes.route('/api/v1/subscription', methods=['PUT'])
@required_partner_authentication
def extend_subscription():
    try:
        # Parse request payload
        payload = request.get_json()
        external_id, duration, expiration_date = (
            payload.get('external_id'),
            payload.get('duration'),
            payload.get('expiration_date'),
        )
    
        # Validate request payload
        if not external_id or not duration or not expiration_date:
            return handle_error('Invalid payload', 400)

        # Check if the subscription exists
        if not get_subscription_by_user_external_id(external_id):
            return handle_error('Subscription not found', 404)

        # Extend subscription
        subscription = get_subscription_by_user_external_id(external_id)
        subscription.duration = duration
        subscription.expiration_date = expiration_date
        update_subscription(subscription)
        
        return jsonify({'message': 'Subscription extended successfully'}), 200

    except Exception as e:
        return handle_error(str(e), 500)
