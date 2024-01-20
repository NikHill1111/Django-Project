from django.db import models

# Create your models here.
class Todo(models.Model):
        todo=models.CharField(max_lenght=50)
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)
        done=models.BooleanField(defaut=False)