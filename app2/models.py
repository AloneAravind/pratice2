from django.db import models

# Create your models here.
class sample(models.Model):
    name = models.CharField(max_length= 50, default= "hello")
    age = models.IntegerField( default= 1) # we are calling integer field in here
    resume = models.FileField( default= "hello")
    email_id = models.EmailField( default= "hello")
    Link = models.URLField( default= "hello")
    phone_no = models.IntegerField(null= True, default= 1)
    gender = models.CharField(max_length = 20,null = True, default= "hello")
# used to save what we need(default it save as object)
    def  __str__(self):
        return self.name #instead of name we can use age,other names
    