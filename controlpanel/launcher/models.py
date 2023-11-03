from django.db import models
# Create your models here.
class Process(models.Model):

    name = models.CharField(max_length=200)
    status = models.BooleanField()
    path = models.CharField(max_length=200, default="/controlled_programs/basic_gui.py")

    def __str__(self):
        return self.name