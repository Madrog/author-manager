import json 
from api.utils.test_base import BaseTestCase
from api.models.users import User
from datetime import datetime
import unittest2 as unittest
from api.utils.token import generate_verification_token, confirm_verification_token


def create_users():
    user1 = User(email="kunal.relan12@gmail.com",username='kunalrelan12',password=User.generate_hash('helloworld'),isVerified=True).create()
    user2 = User(email="kunal.rela123@gmail.com",username='kunalrelan123',password=User.generate_hash('helloworld')).create()


class TestUsers(BaseTestCase):
    def setUp(self):
        super(TestUsers, self).setUp()
        create_users()

    def test_login_user(self):
        user = {
            "email": "kunal.relan12@gmail.com",
            "password": "helloworld"
        }
        response = self.app.post('/api/users/login', data=json.dumps(user), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertTrue('access_token' in data)




if __name__ == '__main__':
    unittest.main()


