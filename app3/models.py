from django.db import models

class employ(models.Model):
    name = models.CharField(max_length= 30)
    reg_num = models.BigIntegerField()
    email = models.EmailField()
    address = models.TextField(null = True)

