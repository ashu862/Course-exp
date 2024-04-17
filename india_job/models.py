from django.db import models

# Create your models here.
class Jobs(models.Model):
    name = models.CharField(max_length=200,null=False)
    exp= models.IntegerField(default=0)
    nop = models.IntegerField(default=0)
    location=models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.name

class Resume(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume_file = models.FileField(upload_to='resumes/')
    role = models.CharField(max_length=100, default='data', choices=(
        ('Tech', 'Tech'),
        ('Sales', 'Sales'),
        ('Data', 'Data'),
    ))
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
class Inquiry(models.Model):
    name = models.CharField(max_length=200,null=False)
    phone= models.IntegerField(default=0)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Mail(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email

    