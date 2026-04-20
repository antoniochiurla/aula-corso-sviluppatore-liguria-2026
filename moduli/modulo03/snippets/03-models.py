from django.db import models


# --- CLASSE BASE: TASK ---
class Task(models.Model):
    # Definiamo gli stati possibili (come avevamo fatto con la logica)
    class Status(models.TextChoices):
        OPEN = 'AP', 'Aperto'
        CLOSED = 'CL', 'Completato'

    title = models.CharField(max_length=200, verbose_name="Titolo")
    description = models.TextField(blank=True, verbose_name="Descrizione")
    created_at = models.DateTimeField(auto_now_add=True)  # Data automatica alla creazione
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.OPEN
    )

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