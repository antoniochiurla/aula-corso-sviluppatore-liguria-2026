from django.contrib.auth.models import User

from tasks.models import Task

def create_admin():
    if not User.objects.filter(username='admin').exists():
        my_admin = User.objects.create_superuser('admin', 'admin@admin.com', "admin")
    else:
        my_admin = User.objects.get(username='admin')

    print('create_admin:', my_admin)
    return my_admin

def create_dev1():
    if not User.objects.filter(username='dev1').exists():
        dev1 = User.objects.create_user(username="dev1", password="dev1")
        dev1.is_staff = True
        dev1.save()
    else:
        dev1 = User.objects.get(username='dev1')
    print('create_dev1:', dev1)
    return dev1
