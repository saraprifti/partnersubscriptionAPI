from app.models import Subscription, User

subscriptions = {}
users = {}

def store_user(user):
    users[user.uuid] = user

def store_subscription(subscription):
    subscriptions[subscription.uuid] = subscription

def update_subscription(subscription):
    subscriptions[subscription.uuid] = subscription

def get_subscription_by_user_external_id(external_id):
    for subscription in subscriptions.values():
        if subscription.user.external_id == external_id:
            return subscription
    return None