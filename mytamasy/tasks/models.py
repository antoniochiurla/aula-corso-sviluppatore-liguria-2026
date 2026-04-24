from django.db import models
from django.contrib.auth.models import User

class TaskType(models.TextChoices):
    TASK = 'T', 'Task'
    BUG = 'B', 'Bug'
    FEATURE = 'F', 'Feature'

# --- CLASSE BASE: TASK ---
class Task(models.Model):
    # Definiamo gli stati possibili (come avevamo fatto con la logica)
    class Status(models.TextChoices):
        OPEN = 'AP', 'Aperto'
        CLOSED = 'CL', 'Completato'

    title = models.CharField(max_length=200, verbose_name="Titolo")
    description = models.TextField(blank=True, verbose_name="Descrizione")
    created_at = models.DateTimeField(auto_now_add=True)  # Data automatica alla creazione
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.OPEN
    )
    type = models.CharField(choices=TaskType.choices, default=TaskType.TASK)
    # bug = models.ForeignKey("BugTask", on_delete=models.CASCADE)
    # feature = models.ForeignKey("FeatureTask", on_delete=models.CASCADE)

    def __str__(self):
        # Questo decide cosa vedremo nel pannello Admin (es. il titolo del task)
        return self.title


# --- SOTTOCLASSE: BUG ---
class BugTask(Task):
    class Severity(models.TextChoices):
        LOW = 'LO', 'Bassa'
        MEDIUM = 'ME', 'Media'
        HIGH = 'HI', 'Alta'

    severity = models.CharField(
        max_length=2,
        choices=Severity.choices,
        default=Severity.LOW,
        verbose_name="Severità"
    )

    def save(self, *args, **kwargs):
       self.type = TaskType.BUG
       super(Task, self).save(*args, **kwargs)



# --- SOTTOCLASSE: FEATURE ---
class FeatureTask(Task):
    class Priority(models.TextChoices):
        LOW = '1', 'Bassa'
        NORMAL = '2', 'Normale'
        URGENT = '3', 'Urgente'

    priority = models.CharField(
        max_length=1,
        choices=Priority.choices,
        default=Priority.NORMAL,
        verbose_name="Priorità"
    )

    def save(self, *args, **kwargs):
       self.type = TaskType.FEATURE
       super(Task, self).save(*args, **kwargs)
