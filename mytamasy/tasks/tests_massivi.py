from django.test import TestCase
from django.contrib.auth.models import User

from tasks.util_tests import create_admin, create_dev1
from tasks.models import Task


class TaskTestCase(TestCase):
    dev1 = None

    @classmethod
    def setUpClass(cls):
        my_admin = create_admin()
        TaskTestCase.dev1 = create_dev1()
        # creo dati fastidiosi agli altri test
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        # elimino i dati fastidiosi
        return super().tearDownClass()


    def setUp(self):
        print("setUp")
        # mi connetto ad un server remoto
        for num_task in range(1000):
            task_n = Task.objects.create(
                                created_by=TaskTestCase.dev1,
                                title="Titolo " + str(num_task),
                                description="Descrizione " + str(num_task),
                                status=Task.Status.OPEN
                            )
        print("end SetUp")
    
    def tearDown(self):
        # mi disconnetto dal server remoto
        return super().tearDown()

    def test_task_count(self):
        task_titolo_query = Task.objects.filter(title__icontains='Titolo')
        self.assertEqual(1000, task_titolo_query.count())

    def test_task_delete(self):
        task_to_delete = Task.objects.get(title='Titolo 65')
        task_to_delete.delete()
        task_titolo_query = Task.objects.filter(title__icontains='Titolo')
        self.assertEqual(999, task_titolo_query.count())

    def test_task_delete_another(self):
        task_to_delete = Task.objects.get(title='Titolo 67')
        task_to_delete.delete()
        task_titolo_query = Task.objects.filter(title__icontains='Titolo')
        self.assertEqual(999, task_titolo_query.count())
