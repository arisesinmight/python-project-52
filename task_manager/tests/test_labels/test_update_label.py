from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.users.models import User


class UpdateStatusTest(TestCase):

    def setUp(self):
        test_label = Label.objects.create(name='Чмо')
        test_label.save()

        test_user = User.objects.create_user(
            first_name='Leha',
            last_name="Bulankov",
            username='avavav',
            password='av13')
        test_user.save()


    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('label_update', kwargs={'pk': 1}))
        self.assertRedirects(resp, '/login/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='avavav', password='av13')
        resp = self.client.get(reverse('label_update', kwargs={'pk': 1}))

        self.assertEqual(str(resp.context['label']), 'Чмо')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'labels/label_update.html')

    def test_label_updated(self):
        self.client.login(username='avavav', password='av13')
        self.client.post(
            reverse('label_update', kwargs={'pk': 1}), {'name': 'пидор'})
        test_label = Label.objects.get(id=1)
        new_data = test_label.name

        self.assertEqual(new_data, 'пидор')







