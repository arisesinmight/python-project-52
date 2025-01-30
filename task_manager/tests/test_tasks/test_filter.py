from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class FilterTest(TestCase):

    def setUp(self):
        test_user_one = User.objects.create_user(
            first_name='Leha',
            last_name="Bulankov",
            username='avavav',
            password='av13')
        test_user_one.save()

        test_user_another = User.objects.create_user(
            first_name='Sanya',
            last_name="Shkurin",
            username='pinki',
            password='sh88')
        test_user_another.save()

        test_status = Status.objects.create(name='111')
        test_status.save()

        test_task_ones = Task.objects.create(
            name='111',
            description='111',
            status=test_status,
            executor=test_user_one,
            author=test_user_one
        )
        test_task_ones.save()

        test_task_anothers = Task.objects.create(
            name='222',
            description='111',
            status=test_status,
            executor=test_user_another,
            author=test_user_another
        )
        test_task_anothers.save()

    def test_own_tasks(self):
        self.client.login(username='avavav', password='av13')
        resp = self.client.get(
            reverse('tasks_index'), {
                'status': 1,
                'only_users_tasks': True
            }
        )
        filtered_list = resp.context['tasks']
        user_ones_tasks = User.objects.get(id=1).created_tasks.all()

        self.assertEqual(list(user_ones_tasks), list(filtered_list))

    def test_anothers_tasks(self):
        self.client.login(username='avavav', password='av13')
        resp = self.client.get(
            reverse('tasks_index'), {
                'status': 1,
                'executor': 2,
                'only_users_tasks': True
            }
        )
        filtered_list = resp.context['tasks']
        user_anothers_tasks = User.objects.get(id=2).created_tasks.all()

        self.assertNotEqual(list(user_anothers_tasks), list(filtered_list))

    def test_on_common(self):
        self.client.login(username='avavav', password='av13')
        resp = self.client.get(
            reverse('tasks_index'), {
                'status': 1,
                'only_users_tasks': False
            }
        )
        filtered_list = resp.context['tasks']

        self.assertEqual(len(filtered_list), 2)
