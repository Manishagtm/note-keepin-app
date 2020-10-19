from django.db import models


class Task (models.Model):
    note_title = models.CharField(max_length=30)
    note_description = models.CharField(max_length=350)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note_title


