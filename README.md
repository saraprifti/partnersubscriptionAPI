# Partner Subscription API

This is an API implementation in Python using Flask framework for managing subscriptions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Authentication](#authentication)
- [Testing](#testing)

## Installation

1. Clone the repository `git clone https://github.com/your/repository.git`
2. Install requirements `pip install -r requirements.txt`
3. Run `python3 -m venv .venv`
3. Run `. .venv/bin/activate`
4. Serve `python -m flask --app run run`

## Endpoints

1. Create Subscription
Endpoint: `POST /api/v1/subscription`

Description: Creates a new subscription for a user.

Request Payload:
`{
  "external_id": "user123",
  "user_email": "user@example.com",
  "subscription_info": {
    "duration": "365",
    "expiration_date": "2024-07-01"
  }
}`

Response:
201 Created if the subscription is created successfully.
401 Unauthorized if the authentication fails.
400 Bad Request if the request payload is invalid.

2. Extend Subscription
Endpoint: `PUT /api/v1/subscription`
Description: Extends an existing subscription for a user.

Request Payload:
{
  "external_id": "user123",
  "subscription_info": {
    "duration": "90",
    "expiration_date": "2023-09-30"
  }
}

Response:
200 OK if the subscription is extended successfully.
401 Unauthorized if the authentication fails.
400 Bad Request if the request payload is invalid.
404 Not Found if the subscription is not found.

## Authentication
API requests should include the following headers for authentication:

X-Partner-ID: The partner's ID.
X-Secret: The shared secret associated with the partner's ID.
The server verifies the authenticity of the requests by matching the partner ID and shared secret.

## Testing

Run command: `python -m unittest discover -s tests -p subscription_tests.py`