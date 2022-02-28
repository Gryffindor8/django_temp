from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import signout, signin, home

class TestUrls(SimpleTestCase):

    def test_sigin_url_is_resolved(self):
        url = reverse('auth:login')
        self.assertEqual(resolve(url).func, signin)

    def test_sigout_url_is_resolved(self):
        url = reverse('auth:signout')
        self.assertEqual(resolve(url).func, signout)

    def test_home_url_is_resolved(self):
        url = reverse('auth:home')
        self.assertEqual(resolve(url).func, home)