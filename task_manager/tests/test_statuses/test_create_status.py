from django.test import TestCase
from task_manager.statuses.models import Status
from task_manager.users.models import User
from django.urls import reverse


class CreateStatusTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            first_name='Leha',
            last_name="Bulankov",
            username='avavav',
            password='av13')
        test_user.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('status_create'))
        self.assertRedirects(resp, '/login/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='avavav', password='av13')
        resp = self.client.get(reverse('status_create'))

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'statuses/status_create.html')

    def test_create_status(self):
        self.client.login(username='avavav', password='av13')
        self.client.post(
            reverse('status_create'), {'name': 'Чмошник'})
        test_status = Status.objects.get(id=1)

        self.assertTrue(test_status)
