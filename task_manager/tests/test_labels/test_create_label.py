from django.test import TestCase
from task_manager.labels.models import Label
from task_manager.users.models import User
from django.urls import reverse


class CreateLabelTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            first_name='Leha',
            last_name="Bulankov",
            username='avavav',
            password='av13')
        test_user.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('label_create'))
        self.assertRedirects(resp, '/login/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='avavav', password='av13')
        resp = self.client.get(reverse('label_create'))

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'labels/label_create.html')

    def test_create_label(self):
        self.client.login(username='avavav', password='av13')
        self.client.post(
            reverse('label_create'), {'name': 'Метка'})
        test_label = Label.objects.get(id=1)

        self.assertTrue(test_label)
