from functools import wraps
from flask import request, Response

class PartnerAuthenticationMiddleware:
    def __init__(self, app, shared_secrets):
        self.app = app
        self.shared_secrets = shared_secrets
        
    def required_authentication(self, func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            partner_id = request.headers.get('X-Partner-ID')
            partner_secret = request.headers.get('X-Secret')

            response = self.check_credentials(partner_id, partner_secret)
            if response:
                return response

            return func(*args, **kwargs)

        return decorated_function

    def check_credentials(self, partner_id, partner_secret):
        if not partner_id or not partner_secret:
            return Response('Unauthorized', mimetype='text/plain', status=401)

        if partner_id not in self.shared_secrets or self.shared_secrets[partner_id] != partner_secret:
            return Response('Unauthorized', mimetype='text/plain', status=401)

 
