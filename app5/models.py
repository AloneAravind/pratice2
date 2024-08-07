from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    

    def _str_(self):
        return self.name 
    