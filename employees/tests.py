from django.test import TestCase

from django.contrib.auth.models import User

from .models import Employee

class EmployeeTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

        test_employee = Employee.objects.create(
            author=testuser1, first_name='ramlal', last_name="marz")
        test_employee.save()

    def test_blog_content(self):
        employee = Employee.objects.get(id=1)
        author = f'{employee.author}'
        first_name = f'{employee.first_name}'
        last_name = f'{employee.last_name}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(first_name, 'ramlal')
        self.assertEqual(last_name, 'marz')