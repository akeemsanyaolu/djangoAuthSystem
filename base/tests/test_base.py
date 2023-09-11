from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import Client

class TestUserRegistration(TestCase):
    def test_user_registration_valid_data(self):
        data = {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_registration_invalid_data(self):
        # Test user registration with invalid data
        data = {
            'username': '',  # Username is required
            'password1': 'password123',
            'password2': 'password456',  # Passwords do not match
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)  # Registration form should be displayed again
        self.assertFalse(User.objects.filter(username='').exists())  # User should not be created

    def test_user_is_authenticated(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        self.client.post(reverse('login'), data)
        response = self.client.get(reverse('register'))
        self.assertRedirects(response, reverse('home'))

    def test_unauthenticated_user(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

class TestUserLoginLogout(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_user_login_valid_credentials(self):
        # Test user login with valid credentials
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)  # Redirect to success page or home
        self.assertTrue(self.client.session['_auth_user_id'])  # User should be authenticated

    def test_user_login_invalid_credentials(self):
        # Test user login with invalid credentials
        data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)  # Login form should be displayed again
        self.assertFalse(self.client.session.get('_auth_user_id'))  # User should not be authenticated

    def test_user_logout(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Test user logout
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect to success page or home
        self.assertFalse(self.client.session.get('_auth_user_id'))  # User should be logged out


class TestHomeView(TestCase):
    def test_home_view_authenticated_user(self):
        # Create and log in a user
        user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Access the home view, it should return a successful response
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_unauthenticated_user(self):
        # Access the home view when not authenticated, it should redirect to the login page
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, reverse('login'))

class TestSessionFixation(TestCase):
    def test_session_id_changes_on_login(self):
        # Create a user
        user = get_user_model().objects.create_user(username='testuser', password='testpassword')

        # Log in the user and get their session ID
        self.client.login(username='testuser', password='testpassword')
        original_session_id = self.client.session.session_key

        # Log out the user
        self.client.logout()

        # Log in the user again and get their new session ID
        self.client.login(username='testuser', password='testpassword')
        new_session_id = self.client.session.session_key

        # Check if the session ID changes after login
        self.assertNotEqual(original_session_id, new_session_id)
