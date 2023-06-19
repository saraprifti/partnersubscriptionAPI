from app.utils import create_unique_uuid #using this method as I am not using a database

subscriptions = {}

class User:
    def __init__(self, external_id, email):
        self.uuid  = create_unique_uuid()
        self.external_id = external_id
        self.email = email
    
class Subscription:
    def __init__(self, user, duration, expiration_date):
        self.uuid  = create_unique_uuid()
        self.user = user
        self.duration = duration
        self.expiration_date = expiration_date
