from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import landing_page, file_view


class TestUrls(SimpleTestCase):

    def test_sigin_url_is_resolved(self):
        url = reverse('core:landing-page')
        self.assertEqual(resolve(url).func, landing_page)

    def test_sigout_url_is_resolved(self):
        url = reverse('core:file_view')
        self.assertEqual(resolve(url).func, file_view)
