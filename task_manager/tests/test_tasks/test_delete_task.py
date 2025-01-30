from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class DeleteTaskTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(
            first_name='Leha',
            last_name="Bulankov",
            username='avavav',
            password='av13')
        test_user.save()

        test_status = Status.objects.create(name='Чмо')
        test_status.save()

        test_task = Task.objects.create(
            name='111',
            description='111',
            status=test_status,
            executor=test_user,
            author=test_user
        )
        test_task.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('task_delete', kwargs={'pk': 1}))
        self.assertRedirects(resp, '/login/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='avavav', password='av13')
        resp = self.client.get(reverse('task_delete', kwargs={'pk': 1}))

        self.assertEqual(str(resp.context['task']), '111')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'tasks/task_delete.html')

    def test_task_deleted(self):
        self.client.login(username='avavav', password='av13')
        self.client.post(reverse('task_delete', kwargs={'pk': 1}))

        self.assertFalse(Task.objects.filter(pk=1))
