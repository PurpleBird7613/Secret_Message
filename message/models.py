from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
	body = models.TextField(max_length=10000,null = True,blank=True)
	file = models.FileField(upload_to="files/",null = True,blank=True)
	password = models.CharField(max_length=30,null = False,blank=False)
	message_link = models.TextField(null = True,blank=True)
	date = models.DateTimeField(auto_now_add = True,verbose_name="created on")
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	

# Getting Password for API Show Message
class Show_Message_Password(models.Model):
    password = models.CharField(max_length = 30,null = False,blank = False)
    date = models.DateTimeField(auto_now_add = True,verbose_name="created on")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
