from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
    path('logout/', views.logout_view, name='logout'),
    path('add/<str:tipo>/', views.add_task, name='add_task'), # Aggiunta
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'), # Modifica
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'), # Cambio stato
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'), # Rimozione
]
