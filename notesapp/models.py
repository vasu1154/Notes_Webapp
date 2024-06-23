from django.db import models

# Create your models here.
class Notes(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title