from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_url(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b"<html>"))
        self.assertIn(b"<title>To-Do lists</title>", response.content)
        self.assertTrue(response.content.strip().endswith(b"</html>"))

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
        # .decode is used to turn the page bytes into string syntax
        # to compare strings