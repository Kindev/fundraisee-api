from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.managers import account_manager


class AccountsTestCase(APITestCase):
    def setUp(self):
        # We want to go ahead and originally create a user.
        self.test_user = account_manager.create_user('test', 'test@endilie.com', 'anythingcanlah')

        # URL for creating an account.
        self.create_url = reverse('user-register')

        # URL for logging in
        self.login_url = reverse('user-login')

        # URL for logging out
        self.logout_url = reverse('user-logout')

        # URL for updating account
        self.update_url = reverse('user-update', kwargs={'username':'test'})

    def test_create_user(self):
        data = {
            'username': 'endiliey',
            'email': 'endiliey@gmail.com',
            'password': 'somepassword'
        }
        prev_cnt = User.objects.count()
        response = self.client.post(self.create_url, data)
        self.assertEqual(User.objects.count(), prev_cnt + 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)

    def test_create_user_with_too_long_username(self):
        data = {
            'username': 'finfinfin'*10,
            'email': 'asdfg@gmail.com',
            'password': 'foobar'
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)

    def test_create_user_with_no_username(self):
        data = {
            'username': '',
            'email': 'ntu@example.com',
            'password': 'foobarbaz'
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)

    def test_create_user_with_preexisting_username(self):
        data = {
            'username': 'test',
            'email': 'user@example.com',
            'password': 'testuser'
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['username']), 1)

    def test_create_user_with_no_password(self):
        data = {
            'username': 'albertlucianto',
            'email': 'test@albert.com',
            'password': ''
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)

    def test_create_user_with_preexisting_email(self):
        data = {
            'username': 'testuser2',
            'email': 'test@endilie.com',
            'password': 'testuser'
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)

    def test_create_user_with_invalid_email(self):
        data = {
            'username': 'foobarbaz',
            'email':  'testing',
            'passsword': 'foobarbaz'
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)

    def test_create_user_with_no_email(self):
        data = {
                'username' : 'foobar',
                'email': '',
                'password': 'foobarbaz'
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)

    def test_login_user(self):
        data = {
            'username': 'test',
            'email': 'test@endilie.com',
            'password': 'anythingcanlah'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_with_wrong_password(self):
        data = {
            'username': 'test',
            'email': 'test@endilie.com',
            'password': 'testtesttest'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_loggedin_user_can_logout(self):
        self.client.force_login(user=self.test_user)
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_not_loggedin_user_cant_logout(self):
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_user(self):
        data = {
            'username': 'test',
            'email': 'test@endilie.com',
            'current_password': 'anythingcanlah',
            'new_password': 'testtest',
            'avatar': '',
        }
        self.client.force_login(user=self.test_user)
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.test_user.refresh_from_db()
        self.assertTrue(self.test_user.check_password('testtest'))
