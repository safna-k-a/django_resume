from django.db import models

# Create your models here.
class resume(models.Model):  
    name= models.CharField(max_length=200)  
    email=models.EmailField(max_length=50)
    aboutyou=models.TextField(max_length=500)
    degree=models.TextField(max_length=500)
    school=models.TextField(max_length=500)
    university=models.TextField(max_length=500)
    experience=models.TextField(max_length=500)
    skills=models.TextField(max_length=500)
    image = models.ImageField(upload_to='images')  
    phone=models.BigIntegerField()
  
    def __str__(self):  
        return self.name 