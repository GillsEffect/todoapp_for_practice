from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Başlık')
    body = models.TextField(verbose_name = 'İçerik')
    check = models.BooleanField(null = True, verbose_name = 'Tamamlandı')

    def __str__(self):
        return self.title

    def isTrue(self):
        if self.check:
            return True
        return False
