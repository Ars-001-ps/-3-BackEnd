import os
import django
from todo.models import Task
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_todo.settings')
django.setup()


Task.objects.create(title="Задача 1", description="Описание 1")
Task.objects.create(title="Задача 2", description="Описание 2")
Task.objects.create(title="Задача 3", description="Описание 3")

tasks = Task.objects.all()
for t in tasks:
    print(t.id, t.title, t.completed)

task = Task.objects.get(id=1)
task.completed = True
task.save()
print("Задача 1 обновлена:", task.completed)

Task.objects.get(id=2).delete()
print("Задача 2 удалена")
