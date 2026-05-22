from django.test import TestCase
from django.contrib.auth.models import User

from tasks.models import Task
from tasks.util_tests import create_admin, create_dev1


class TaskTestCase(TestCase):
    dev1 = None
    task1_title = "Crea il progetto"
    task1_description = "Il progetto consiste in un Task Management System"
    task2_title = "Crea il repository per il progetto"
    task2_description = "Crea un repository git su github"

    @classmethod
    def setUpClass(cls):
        my_admin = create_admin()
        TaskTestCase.dev1 = create_dev1()

        Task.objects.create(
            created_by=TaskTestCase.dev1,
            title=TaskTestCase.task1_title,
            description=TaskTestCase.task1_description,
            status=Task.Status.OPEN
            )
        Task.objects.create(
            created_by=TaskTestCase.dev1,
            title=TaskTestCase.task2_title,
            description=TaskTestCase.task2_description,
            status=Task.Status.OPEN
            )
        print("end SetUpClass")
        return super().setUpClass()
    
    def setUp(self):
        print("setUp")
        print("end SetUp")

    def test_crea_il_progetto(self):
        """Il primo task deve essere presente"""
        task_crea_progetto = Task.objects.get(title=TaskTestCase.task1_title)
        self.assertEqual(task_crea_progetto.description, TaskTestCase.task1_description)

    def test_str_corretto(self):
        """La conversione a string di un task ha un determinato formato"""
        task_crea_progetto = Task.objects.get(title=TaskTestCase.task1_title)
        self.assertEqual(str(task_crea_progetto), f'T: {TaskTestCase.task1_title}')

    def test_crea_il_repository(self):
        """Il secondo task deve essere presente"""
        task_crea_repository = Task.objects.get(title=TaskTestCase.task2_title)
        self.assertEqual(task_crea_repository.description, TaskTestCase.task2_description)

    def test_create_another_task(self):
        another_task = Task.objects.create(
            created_by=TaskTestCase.dev1,
            title="Altro task",
            description="desc",
            status=Task.Status.OPEN
            )
        all_task_query = Task.objects.all()
        self.assertEqual(3, all_task_query.count())

    def test_check_tasks_count(self):
        all_task_query = Task.objects.all()
        self.assertEqual(2, all_task_query.count())

