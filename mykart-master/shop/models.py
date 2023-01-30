from django.db import models


# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=100)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    name = models.CharField(max_length=30, default=None)
    phone = models.BigIntegerField(default=0)
    email = models.EmailField(max_length=39, default=None)
    query = models.CharField(max_length=300, default=None)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000,default=None)
    name = models.CharField(max_length=111,default=None)
    email = models.CharField(max_length=111,default=None)
    address = models.CharField(max_length=111,default=None)
    city = models.CharField(max_length=111,default=None)
    state = models.CharField(max_length=111,default=None)
    zipcode = models.CharField(max_length=111,default=None)
    phone = models.BigIntegerField(default=0)


class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."
