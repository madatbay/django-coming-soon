from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.

class Setting(models.Model):
    title = RichTextField(max_length=300)
    describtion =RichTextField(max_length=260)
    timer = models.CharField(max_length=150)
    button_text = models.CharField(max_length=36, null=True)
    modal_title = models.CharField(max_length=150, null=True)
    modal_describtion = RichTextField(max_length=150, null=True)
    facebook = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    telegram = models.CharField(max_length=150)
    logo = models.ImageField(null=True, blank=True, upload_to='logo/' )

    def __str__(self):
        return self.title

class Notify(models.Model):
    email = models.EmailField(max_length=140)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.email