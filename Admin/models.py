from django.db import models
# Create your models here.

class Category(models.Model):
    category_name=models.CharField(unique=True,max_length=50,)

    def __str__(self):
        return self.category_name
    
    class Meta:
        db_table="Category"
    
class Gender(models.Model):
    gender=models.CharField(max_length=20)
    genderimage=models.ImageField(upload_to="image")

    def __str__(self):
        return self.gender

    class Meta:
        db_table="Gender"

class Brand(models.Model):
    brand=models.CharField(max_length=20)
    brandimage=models.ImageField(upload_to="image")

    def __str__(self):
        return self.brand

    class Meta:
        db_table="Brand"


class Type(models.Model):
    Type=models.CharField(max_length=20)

    def __str__(self):
        return self.Type

    class Meta:
        db_table="Type"
   
class Watch(models.Model):
    
    watch_model=models.CharField(max_length=200)
    price=models.FloatField(default=1000)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    description=models.CharField(max_length=1000,default="")
    image=models.ImageField(upload_to="image",default="abc.jpg")
    gender=models.ForeignKey(Gender,on_delete=models.CASCADE)
    band=models.CharField(max_length=20,default="Leather")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    Type=models.ForeignKey(Type,on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.watch_model

    class Meta :
        db_table="Watch"

class Payment(models.Model):
    card_no=models.CharField(max_length=4)
    cvv=models.CharField(max_length=4)
    expiry=models.CharField(max_length=10)
    balance=models.FloatField(default=10000)

    class Meta:
        db_table=('Payment')
