from django.db import models
import datetime
class vebblerservice(models.Model):
    name=models.CharField(max_length=250)
    date=models.DateTimeField(default=datetime.datetime.now)
    cost=models.IntegerField()
    contact=models.IntegerField()

class vebbler_coustmer_info(models.Model):
    name=models.CharField(max_length=250)
    addres=models.CharField(max_length=250)
    contact=models.IntegerField()
    email=models.EmailField(default='aaaaaaaa@gmail.com')

class vebbler_ios_services(models.Model):
    company=models.CharField(max_length=250)
    name=models.IntegerField()
    device=models.CharField(max_length=250)

class vebbler_jobinfo(models.Model):
    name=models.CharField(max_length=55)
    feedback=models.TextField()
    mobile=models.IntegerField()
    addres=models.CharField(max_length=250)


