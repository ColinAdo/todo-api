from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo

class TodoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title = 'Test Title',
            body = 'Test body',
        )

    def test_todo_content(self):
        self.assertEqual(self.todo.title, 'Test Title')
        self.assertEqual(self.todo.body, 'Test body')
        self.assertEqual(self.todo.__str__(), 'Test Title')

    def test_api_listview(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertEqual(Todo.objects.count(), 1) 
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(
            reverse('todo_detail', kwargs={'pk': self.todo.id}), 
            format='json'
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

