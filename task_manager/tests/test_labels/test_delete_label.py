from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class DeleteLabelTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            first_name='Leha',
            last_name="Bulankov",
            username='avavav',
            password='av13')
        test_user.save()

        test_label = Label.objects.create(name='222')
        test_label.save()

        test_status = Status.objects.create(name='222')
        test_status.save()

        test_task = Task.objects.create(
            name='111',
            description='111',
            status=test_status,
            executor=test_user,
            author=test_user,
        )
        test_task.labels.add(test_label)
        test_task.save()


    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('label_delete', kwargs={'pk': 1}))
        self.assertRedirects(resp, '/login/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='avavav', password='av13')
        resp = self.client.get(reverse('label_delete', kwargs={'pk': 1}))

        self.assertEqual(str(resp.context['label']), '222')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'labels/label_delete.html')

    def label_in_use(self):
        self.client.login(username='avavav', password='av13')
        resp = self.client.get(reverse('label_delete', kwargs={'pk': 1}))
        self.client.post(reverse('status_delete', kwargs={'pk': 1}))

        self.assertEqual(resp.status_code, 302)
        self.assertTrue(Label.objects.filter(pk=1))


    def test_label_deleted(self):
        self.client.login(username='avavav', password='av13')
        self.client.post(reverse('task_delete', kwargs={'pk': 1}))

        self.client.post(reverse('label_delete', kwargs={'pk': 1}))

        self.assertFalse(Label.objects.filter(pk=1))




