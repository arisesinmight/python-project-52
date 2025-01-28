from django.test import TestCase
from task_manager.users.models import User
from django.urls import reverse


class DeleteUserTest(TestCase):

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
        resp = self.client.get(reverse('user_delete', kwargs={'pk': 1}))
        self.assertRedirects(resp, '/login/')

    def test_permission_denied(self):
        self.client.login(username='avavav', password='av13')
        resp = self.client.get(reverse('user_delete', kwargs={'pk': 2}))

        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/users/')


    def test_logged_in_uses_correct_template(self):
        self.client.login(username='avavav', password='av13')
        resp = self.client.get(reverse('user_delete', kwargs={'pk': 1}))

        self.assertEqual(str(resp.context['user']), 'Leha Bulankov')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/user_delete.html')

    def test_user_deleted(self):
        self.client.login(username='avavav', password='av13')
        self.client.post(reverse('user_delete', kwargs={'pk': 1}))

        self.assertFalse(User.objects.filter(pk=1))




