from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Başlık')
    completed = models.BooleanField(default=False)
    #add_creator

    def __str__(self):
        return self.title
