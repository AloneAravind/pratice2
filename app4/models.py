from django.db import models


class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email=models.EmailField(null=True)
    date_created= models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    CATEGORY=(('Indoor','Indoor'),('out door','out door'),)
   
    name=models.CharField(max_length=200, null=True)
    price=models. FloatField(null=True)
    category =models. CharField(max_length=200, null=True, choices=CATEGORY) # choices - dropdown
    description =models. CharField(max_length=200, null=True)
    date_created =models.DateTimeField(auto_now_add=True, null=True)
    tags=models. ManyToManyField(Tag) # class name
    
    def __str__(self):
        return self.name
    
    
class Order(models. Model):

    STATUS = (('Pending', 'Pending'),('Out for delivery', 'Out for delivery'),
              ('Delivered', 'Delivered'),)
    # it allows only tuple data type
    customer= models.ForeignKey(Customer, null =True, on_delete= models.SET_NULL)
    product= models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_time =models.DateTimeField(auto_now_add=True, null=True)
    status =models.CharField(max_length=200, null=True, choices=STATUS)
    def __str__(self):
        return f"Order {self.id}"
    
class one(models.Model):
    name = models.CharField(max_length=30)
    emp_id = models.IntegerField()
    def __str__(self):
        return self.name


class many(models.Model):
    emp_name = models.OneToOneField(one,null = True, on_delete= models.CASCADE)
    salary = models.IntegerField()
    role = models.CharField(max_length= 15)

