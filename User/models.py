from django.db import models
from Admin.models import Watch
from datetime import datetime, timedelta
from django.utils import timezone as tz



# Create your models here.

def next_day_dt(n=3):
    return tz.localtime(tz.now()) + tz.timedelta(days=7)

class UserInfo(models.Model):
    name = models.CharField(max_length=30,default="Unknown")
    email = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    
    class Meta:
        db_table="UserInfo"

class MyCard(models.Model):
    user=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    Watch=models.ForeignKey(Watch,on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)

    class Meta:
        db_table="MyCard"

class OrderMaster(models.Model):
    user=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    amount=models.FloatField(default=10000)
    details=models.CharField(max_length=1000)

    class Meta:
        db_table="OrderMaster"

class Review(models.Model):
    user=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    Watch=models.ForeignKey(Watch,on_delete=models.CASCADE)
    content=models.TextField(blank=True,null=True)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    
    def __str__(self):
        return str(self.user) +  " Review: " + self.content

    class Meta:
        db_table="Review"

class CheckoutDetail(models.Model):
   
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    total_amount = models.CharField(max_length=10, blank=True,null=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    orderdate = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.address

    class Meta:
        db_table="CheckoutDetail"
    
class Order(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.SET_NULL, null=True)
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    amount = models.FloatField(default=10000)
    checkoutdetail = models.ForeignKey(CheckoutDetail,default="1",on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100, blank=True)
    delivery_date = models.DateTimeField(default=next_day_dt)
    


    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table="Order"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.name