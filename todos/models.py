from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Başlık')
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=False, auto_now_add = True)
    #add_creator

    def __str__(self):
        return self.title

    def snippet(self):
        return self.title[:50] + '...'

    def isTrue(self):
        if self.check:
            return True
        return False
