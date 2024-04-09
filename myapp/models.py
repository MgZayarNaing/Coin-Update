from django.db import models
import uuid
from datetime import datetime

# Create your models here.

class HeroModel(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(default=None)
    background_image = models.ImageField(default=None)
    image = models.ImageField(default=None)
    time = models.DateTimeField(default=datetime.now)

class UserModel(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(default=None)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    coin_status = models.BooleanField(default=False)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username
    
class CoinTypeModel(models.Model):
    type = models.CharField(max_length=200)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.type

class NetworkModel(models.Model):
    type = models.CharField(max_length=200)
    qrcode = models.ImageField(default=None,null=True,blank=True)
    link_name = models.CharField(max_length=20)
    link_address = models.CharField(max_length=50)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.type
    
class CoinModel(models.Model):
    customer = models.ForeignKey(UserModel,on_delete=models.CASCADE,default=None)
    coin_type = models.ForeignKey(CoinTypeModel,on_delete=models.CASCADE,default=None)
    network_type = models.ForeignKey(NetworkModel,on_delete=models.CASCADE,default=None)
    quantity = models.BigIntegerField(default=0)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.customer.username} has {self.quantity} MMK."    
    
class DepositModel(models.Model):
    customer = models.ForeignKey(UserModel,on_delete=models.CASCADE,default=None)
    coin_type = models.ForeignKey(CoinTypeModel,on_delete=models.CASCADE,default=None)
    network_type = models.ForeignKey(NetworkModel,on_delete=models.CASCADE,default=None)
    quantity = models.BigIntegerField(default=0)
    screenshot = models.ImageField(default=None,null=True,blank=True)
    status = models.BooleanField(default = False)
    time = models.DateTimeField(default=datetime.now)

class WithDrawModel(models.Model):
    customer = models.ForeignKey(UserModel,on_delete=models.CASCADE,default=None)
    coin_type = models.ForeignKey(CoinTypeModel,on_delete=models.CASCADE,default=None)
    network_type = models.ForeignKey(NetworkModel,on_delete=models.CASCADE,default=None)
    quantity = models.BigIntegerField(default=0)
    address = models.TextField(default=None)
    status = models.BooleanField(default = False)
    time = models.DateTimeField(default=datetime.now)

class RandomModel(models.Model):
    a = models.CharField(max_length=20)
    b = models.CharField(max_length=20)
    c = models.CharField(max_length=20)
    room = models.IntegerField(default=None,null=True,blank=True)
    status = models.CharField(default=None,null=True,blank=True,max_length=20)
    roundno = models.IntegerField(default=None,null=True,blank=True)

class UserChoiceModel(models.Model):
    choice = models.CharField(max_length=20)
    amount = models.IntegerField()
    room = models.IntegerField(default=None)
    roundno = models.IntegerField()
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,default=None)
