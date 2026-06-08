from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'bugs', views.BugTaskViewSet)
router.register(r'features', views.FeatureTaskViewSet)

urlpatterns = [
	path("", views.index, name="index"),
	path("lista_con_classe", views.TaskListView.as_view(), name="lista_con_classe"),
    path('logout/', views.logout_view, name='logout'),
    path('add/<str:tipo>/', views.add_task, name='add_task'), # Aggiunta
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'), # Modifica
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'), # Cambio stato
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'), # Rimozione
    path('create_random/', views.create_sample_tasks, name='create_sample_tasks'), # Creazione random
    path('stats/', views.stats, name='stats'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('bulk_assign/', views.bulk_assign, name='bulk_assign'),
    path('api/', include(router.urls)),
    path('ang/', views.angular_index, name='angular_index'),
]
