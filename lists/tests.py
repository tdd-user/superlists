#!/usr/bin/env python

from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

from lists.models import Item

#from pdb import set_trace
#set_trace() 
# pause for a moment to check whatever values

class HomePageTest(TestCase):
       
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_request_returns_correct_html(self):
        response = self.client.get('/')  
        html = response.content.decode('utf8')  
        self.assertTrue(html.strip().startswith('<html>'), "check the home page's html tags")  
        self.assertIn('<title>To-Do lists</title>', html)  
        self.assertTrue(html.strip().endswith('</html>'), "check the home page's html tags")  
        #print(repr(html))
        self.assertTemplateUsed(response, 'home.html')  
        
    def test_user_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        html = response.content.decode('utf8')  
        #print(repr(html))

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
        
        