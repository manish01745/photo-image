from django.db import models

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=200, null=False ,blank=True)
    
    def __str__(self):
        return self.category


class uploder(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    image=models.ImageField(upload_to="image")
    date_time=models.DateTimeField(auto_now_add=True,auto_now=False)
    discription=models.CharField(max_length=200, null=False ,blank=True)
    
    def __str__(self):
        return self.discription

