from django.test import TestCase
from task_manager.users.models import User
from django.urls import reverse
from task_manager.users.views import UserUpdateView


class UpdateUserTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            first_name='Leha',
            last_name="Bulankov",
            username='avavav',
            password='av13')
        test_user.save()

        test_wrong_user = User.objects.create_user(
            first_name='Sanya',
            last_name="Shkurin",
            username='pinki',
            password='sh88')
        test_wrong_user.save()


    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('user_update', kwargs={'pk': 1}))
        self.assertRedirects(resp, '/login/')

    def test_permission_denied(self):
        login = self.client.login(username='avavav', password='av13')
        resp = self.client.get(reverse('user_update', kwargs={'pk': 2}))

        self.assertRedirects(resp, '/users/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='avavav', password='av13')
        resp = self.client.get(reverse('user_update', kwargs={'pk': 1}))

        self.assertEqual(str(resp.context['user']), 'Leha Bulankov')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/update.html')

    '''def test_user_updated(self):
        login = self.client.login(username='avavav', password='av13')
        resp_get = self.client.get(reverse('user_update', kwargs={'pk': 1}))
        resp_post'''




