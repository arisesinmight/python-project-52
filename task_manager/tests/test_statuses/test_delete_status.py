from django.test import TestCase
from task_manager.statuses.models import Status
from task_manager.users.models import User
from django.urls import reverse


class DeleteUserTest(TestCase):

    def setUp(self):
        test_status = Status.objects.create(name='Чмо')
        test_status.save()

        test_user = User.objects.create_user(
            first_name='Leha',
            last_name="Bulankov",
            username='avavav',
            password='av13')
        test_user.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('status_delete', kwargs={'pk': 1}))
        self.assertRedirects(resp, '/login/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='avavav', password='av13')
        resp = self.client.get(reverse('status_delete', kwargs={'pk': 1}))

        self.assertEqual(str(resp.context['status']), 'Чмо')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'statuses/status_delete.html')

    def test_status_deleted(self):
        self.client.login(username='avavav', password='av13')
        self.client.post(reverse('status_delete', kwargs={'pk': 1}))

        self.assertFalse(Status.objects.filter(pk=1))




