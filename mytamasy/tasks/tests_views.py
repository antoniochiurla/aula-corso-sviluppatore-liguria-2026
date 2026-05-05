from django.test import TestCase
from django.urls import reverse

from tasks.models import Task

from tasks.util_tests import create_admin, create_dev1

class TaskViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        my_admin = create_admin()
        TaskViewTest.dev1 = create_dev1()
        return super().setUpClass()


    def test_index_redirect_if_not_logged_in(self):
        """Verifica che un utente anonimo venga rimandato al login (302)"""
        response = self.client.get(reverse('index'))
        # Django di default reindirizza a /accounts/login/?next=/
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_index_access_logged_in(self):
        """Verifica che l'utente 'dev1' loggato possa accedere alla index (200)"""
        # Eseguiamo il login prima del test
        self.client.login(username='dev1', password='dev1')
        
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_add_task_logged_in_assignment(self):
        """Verifica che un nuovo task creato sia assegnato automaticamente a chi scrive"""
        self.client.login(username='dev1', password='dev1')
        
        self.client.post(reverse('add_task', args=['T']), {
            'titolo': 'Task creato da dev1',
            'descrizione': 'Prova'
        })
        
        ultimo_task = Task.objects.last()
        self.assertEqual(ultimo_task.created_by, TaskViewTest.dev1)
        self.assertEqual(ultimo_task.title, 'Task creato da dev1')

    def test_add_bug_task_logged_in_assignment(self):
        """Verifica che un nuovo task di tipo bug creato sia assegnato automaticamente a chi scrive"""
        self.client.login(username='dev1', password='dev1')
        
        self.client.post(reverse('add_task', args=['B']), {
            'titolo': 'Task creato da dev1',
            'descrizione': 'Prova'
        })
        
        ultimo_task = Task.objects.last()
        self.assertEqual(ultimo_task.created_by, TaskViewTest.dev1)
        self.assertEqual(ultimo_task.title, 'Task creato da dev1')
        self.assertEqual(ultimo_task.type, 'B')
        
    def test_add_feature_task_logged_in_assignment(self):
        """Verifica che un nuovo task di tipo feature creato sia assegnato automaticamente a chi scrive"""
        self.client.login(username='dev1', password='dev1')
        
        self.client.post(reverse('add_task', args=['F']), {
            'titolo': 'Task creato da dev1',
            'descrizione': 'Prova'
        })
        
        ultimo_task = Task.objects.last()
        self.assertEqual(ultimo_task.created_by, TaskViewTest.dev1)
        self.assertEqual(ultimo_task.title, 'Task creato da dev1')
        self.assertEqual(ultimo_task.type, 'F')
        