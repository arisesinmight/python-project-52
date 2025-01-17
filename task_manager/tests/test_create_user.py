from django.test import TestCase
from task_manager.users.models import User
from django.urls import reverse
from task_manager.users.views import UserCreateView


class CreateUserTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            first_name='Leha',
            last_name="Bulankov",
            username='avavav',
            password='av13')
        test_user.save()


    def test_correct_template(self):
        resp = self.client.get(reverse('user_create'))

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/create.html')

