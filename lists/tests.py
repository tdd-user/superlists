#!/usr/bin/env python

from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
       
        
    def test_home_page_returns_correct_html(self):

        response = self.client.get('/')  
        html = response.content.decode('utf8')  
        self.assertTrue(html.strip().startswith('<html>'), "check the home page's html tags")  
        self.assertIn('<title>To-Do lists</title>', html)  
        self.assertTrue(html.strip().endswith('</html>'), "check the home page's html tags")  
        print(repr(html))
        self.assertTemplateUsed(response, 'home.html')  
        