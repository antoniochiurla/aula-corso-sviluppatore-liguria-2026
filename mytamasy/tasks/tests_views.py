from django.test import TestCase
from django.urls import reverse

from tasks.models import Task, BugTask, FeatureTask

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

    def test_add_task_get_logged_in_assignment(self):
        """Verifica che la pagina di aggiunta task funzioni"""
        self.client.login(username='dev1', password='dev1')
        
        response = self.client.get(reverse('add_task', args=['T']))
        
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
    
    def test_edit_task_get(self):
        Task.objects.create(
            created_by=TaskViewTest.dev1,
            title='titolo',
            description='descrizione',
            status=Task.Status.OPEN
            )
        task_to_change = Task.objects.last()
        self.client.login(username='dev1', password='dev1')
        response = self.client.get(reverse('edit_task', args=[task_to_change.id]))
        self.assertEqual(response.status_code, 200)


    def test_edit_task_post(self):
        Task.objects.create(
            created_by=TaskViewTest.dev1,
            title='titolo',
            description='descrizione',
            status=Task.Status.OPEN
            )
        task_to_change = Task.objects.last()
        self.client.login(username='dev1', password='dev1')
        titolo_modificato = 'titolo modificato'
        descrizione_modificata = 'descrizione modifcata'
        self.client.post(reverse('edit_task', args=[task_to_change.id]), {
            'titolo': titolo_modificato,
            'descrizione': descrizione_modificata
        })
        task_changed = Task.objects.get(pk=task_to_change.id)
        self.assertEqual(titolo_modificato, task_changed.title)
        self.assertEqual(descrizione_modificata, task_changed.description)

    
    def test_edit_bug_task_get(self):
        BugTask.objects.create(
            created_by=TaskViewTest.dev1,
            title='titolo',
            description='descrizione',
            severity=BugTask.Severity.HIGH,
            status=Task.Status.OPEN
            )
        task_to_change = Task.objects.last()
        self.client.login(username='dev1', password='dev1')
        response = self.client.get(reverse('edit_task', args=[task_to_change.id]))
        self.assertEqual(response.status_code, 200)


    def test_edit_bug_task_post(self):
        BugTask.objects.create(
            created_by=TaskViewTest.dev1,
            title='titolo',
            description='descrizione',
            severity=BugTask.Severity.HIGH,
            status=Task.Status.OPEN
            )
        task_to_change = BugTask.objects.last()
        self.client.login(username='dev1', password='dev1')
        titolo_modificato = 'titolo modificato'
        descrizione_modificata = 'descrizione modifcata'
        self.client.post(reverse('edit_task', args=[task_to_change.id]), {
            'titolo': titolo_modificato,
            'descrizione': descrizione_modificata,
            'severity': 'HIGH'
        })
        task_changed = BugTask.objects.get(pk=task_to_change.id)
        self.assertEqual(titolo_modificato, task_changed.title)
        self.assertEqual(descrizione_modificata, task_changed.description)
