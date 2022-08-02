from datetime import datetime
from django import forms

from django.db import models

# Create your models here.
class Title(models.Model):
    title = models.CharField(max_length=30,default="post it")

    def __str__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=30)
    permalink = models.CharField(max_length=12,unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField(default="this is by-default", blank=True)

    def __str__(self):
        return self.title

class Contactform(models.Model):
    yourname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500, default="type your message")

    def __str__(self):
        return self.yourname

class Profile(models.Model):
    sem = (("1st","1st"),("2nd","2nd"),("3rd","3rd"),("4th","4th"))
    gen = (("male","male"),("female","female"),("other","other"))
    username = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100)
    semester = models.CharField(max_length=10,choices=sem)
    gender = models.CharField(max_length=10,choices=gen)
    profileimage = models.ImageField(upload_to = "profileimage",blank=True)
    profileimagename = models.CharField(blank=True,default="profileimage/",max_length=100)

    def __str__(self):
        return self.username


class UserData(models.Model):
    ch = (("public","public"),("private","private"))
    #id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    username = models.CharField(max_length=50,default="Baibhab@7279")
    email = models.EmailField(max_length=100,default="abc@gmail.com")
    image = models.ImageField(upload_to = "images",blank=True)
    blogtext = models.TextField(default="",max_length=1000)
    uploadtime = models.DateTimeField(default=datetime.now,blank=True)
    choise = models.CharField(blank=True,choices=ch,default="public",max_length=20)
    imagename = models.CharField(blank=True,default="images/",max_length=100)
    
    def __str__(self):
        return self.username

