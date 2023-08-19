from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image



class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE ,related_name='Profile')
    name_f = models.CharField(max_length=200, null=True)
    name_l = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    img = models.ImageField(upload_to='images/%y/%m/%d', default='default/user3.png', blank=True, null=True)
    assistant = models.BooleanField(default=False, blank=True, null=True)
    admin = models.BooleanField(default=False, blank=True, null=True)
    
    def __str__(self):
        return f'{self.user}'
    
    @property
    def imgUser(self):
        if self.img is None:
            url = ''
        else:
            url = self.img.url
        return url
    
class Comment(models.Model):
    user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE ,related_name='Comment')
    commet = models.TextField(max_length=500, null=True , blank=True)
    time = models.DateTimeField(default=datetime.now())
    best = models.BooleanField(default=False, null=True, blank=True)
    favourite = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user}'
    
class UserMsg(models.Model):
    user = models.ForeignKey(Profile, null=True,blank=True, on_delete=models.CASCADE ,related_name='UserMsg')
    name_f = models.CharField(max_length=200, null=True)
    name_l = models.CharField(max_length=200, null=True)
    name_for_nonUser = models.CharField(max_length=300, blank=True, null=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    msg = models.TextField(max_length=500, null=True, blank=True)
    time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        if(self.name_f is not None and self.name_l is not None):
            return f'{self.name_f} {self.name_l} Message'
        else:
            return f'{self.name_for_nonUser} Message'
        
class About(models.Model):
    aboutS1 = models.TextField(max_length=1000, null=True, blank=True, default="Section_1")
    aboutS2 = models.TextField(max_length=1000, null=True, blank=True, default="Section_2")
    aboutS3 = models.TextField(max_length=1000, null=True, blank=True, default="Section_3")
    aboutS4 = models.TextField(max_length=1000, null=True, blank=True, default="Section_4")
    aboutSkills = models.TextField(max_length=1000, null=True, blank=True, default="Skills")
    
class Plog(models.Model):
    logo = models.CharField(max_length=100, null=True, blank=True, default="Logo")
    plogName = models.CharField(max_length=100, null=True, blank=True, default="Plog_Name")
    
    def __str__(self):
        return self.logo
    
class Project(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, default='Project-Name')
    description = models.TextField(max_length=400, null=True, blank=True, default='Project-Description')
    img = models.ImageField(upload_to='projects/%d', default="default/project.png", null=True, blank=True)
    link = models.CharField(max_length=300, null=True , blank=True, default="none")
    html = models.BooleanField(default=False, null=True, blank=True)
    js = models.BooleanField(default=False, null=True, blank=True)
    dj = models.BooleanField(default=False, null=True, blank=True)
    css = models.BooleanField(default=False, null=True, blank=True)
    py = models.BooleanField(default=False, null=True, blank=True)
    bootS = models.BooleanField(default=False, null=True, blank=True)
    bostG = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return self.name
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.img.path)
        
    #     if img.height > 220 or img.width > 377:
    #         output_size = (377,220)
    #         img.thumbnail(output_size)
    #         img.save(self.img.path)
    
class ProjectPhoto(models.Model):
    project = models.OneToOneField(Project,null=True, on_delete=models.CASCADE ,related_name='Project')
    img1 = models.ImageField(upload_to='projects/%d', default="default/project.png", null=True, blank=True)
    img2 = models.ImageField(upload_to='projects/%d', default="default/project.png", null=True, blank=True)
    img3 = models.ImageField(upload_to='projects/%d', default="default/project.png", null=True, blank=True)
    
    def __str__(self):
        return f'{self.project.name}-imgs'
    
    
class SocialLinks(models.Model):
    facebook = models.CharField(max_length=1000, null=True, blank=True)
    instagram = models.CharField(max_length=1000, null=True, blank=True)
    github = models.CharField(max_length=1000, null=True, blank=True)
    linkedin = models.CharField(max_length=1000, null=True, blank=True)
    watsapp = models.CharField(max_length=1000, null=True, blank=True)