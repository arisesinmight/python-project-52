from django.test import TestCase
from task_manager.users.models import User
from django.urls import reverse
from task_manager.users.views import UserCreateView


class CreateUserTest(TestCase):

    def test_correct_template(self):
        resp = self.client.get(reverse('user_create'))

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/user_create.html')

    def test_create_user(self):
        self.client.post(
            reverse('user_create'),
            {'first_name': 'Leha',
             'last_name': 'Bulankov',
             'username': 'avavav',
             'password1': 'av13',
             'password2': 'av13'
             })
        test_user = User.objects.get(id=1)

        self.assertTrue(test_user)
