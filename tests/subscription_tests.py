import unittest
from app.models import User, Subscription
from app.database import (
    users,
    subscriptions,
    store_user,
    store_subscription,
    get_subscription_by_user_external_id,
    update_subscription,
)

class SubscriptionTests(unittest.TestCase):
    def setUp(self):
        # Create test users
        self.user1 = User('external_id_1', 'user1@example.com')
        self.user2 = User('external_id_2', 'user2@example.com')
        # Create test subscriptions
        self.subscription1 = Subscription(self.user1, 30, '2023-06-30')
        self.subscription2 = Subscription(self.user2, 60, '2023-07-31')

    def test_store_user(self):
        # Store test users
        store_user(self.user1)
        store_user(self.user2)
        
        # Assert users are stored correctly
        self.assertEqual(users[self.user1.uuid], self.user1)
        self.assertEqual(users[self.user2.uuid], self.user2)

    def test_store_subscription(self):
        # Store test subscriptions
        store_subscription(self.subscription1)
        store_subscription(self.subscription2)
       
        # Assert subscriptions are stored correctly
        self.assertEqual(subscriptions[self.subscription1.uuid], self.subscription1)
        self.assertEqual(subscriptions[self.subscription2.uuid], self.subscription2)

    def test_get_subscription_by_user_external_id(self):
        # Store test subscriptions
        store_subscription(self.subscription1)
        store_subscription(self.subscription2)
       
        # Retrieve subscription by user external_id
        found_subscription1 = get_subscription_by_user_external_id(self.user1.external_id)
        found_subscription2 = get_subscription_by_user_external_id(self.user2.external_id)
        
        # Assert correct subscriptions are retrieved
        self.assertEqual(found_subscription1, self.subscription1)
        self.assertEqual(found_subscription2, self.subscription2)

    def test_update_subscription(self):
        # Store test subscriptions
        store_subscription(self.subscription1)
        store_subscription(self.subscription2)
        
        # Modify subscription duration and expiration date
        self.subscription1.duration = 90
        self.subscription1.expiration_date = "2023-09-30"
        
        # Update the subscription
        update_subscription(self.subscription1)
        # Retrieve the updated subscription
        updated_subscription = subscriptions[self.subscription1.uuid]
        
        # Assert subscription is updated correctly
        self.assertEqual(updated_subscription.duration, 90)
        self.assertEqual(updated_subscription.expiration_date, "2023-09-30")

if __name__ == '__main__':
    unittest.main()