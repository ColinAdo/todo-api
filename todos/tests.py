from django.test import TestCase

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

