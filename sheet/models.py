from django.db import models

# Create your models here.
class problem(models.Model):
    name = models.CharField(max_length=100)
    problem_id = models.CharField(max_length=10)
    rating = models.IntegerField(default=800)
    link = models.URLField(max_length=200, default='')
    
    def __str__(self):
        return self.name
    
    
class user_handles(models.Model):
    handle = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.handle