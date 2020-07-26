from django.db import models

# Create your models here.

class Contact (models.Model):
    
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    message=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Gallery (models.Model):
    id =models.AutoField(primary_key=True)
    img_name=models.CharField(max_length=30)
    images =models.ImageField(upload_to="login/static/image/")

    def __str__(self):
        return self.img_name