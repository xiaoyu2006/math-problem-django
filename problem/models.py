from django.db import models

# Create your models here.

class Problem(models.Model):
    title=models.TextField(max_length=100)
    text=models.TextField()
    asker=models.TextField(max_length=25)
    img=models.ImageField(upload_to='img', blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Solve(models.Model):
    problem=models.ForeignKey(Problem)
    text=models.TextField()
    name=models.TextField(max_length=25)
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text