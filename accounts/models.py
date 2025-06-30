from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
from django.forms.formsets import formset_factory



class Profile(models.Model):

    class UserRole(models.TextChoices):

        CI = 'CI', 'Citizens'
        OF = 'OF', 'Officer'
        MA = 'MA','Manager'
        A ='A','Admin'


    class GenderChoice(models.TextChoices):
        M = 'M',"Male"
        F = 'F', "Female"
        
    
    
    id = models.PositiveIntegerField(primary_key=True, verbose_name='your adhar number ', unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=2, choices=GenderChoice)
    phone = models.CharField(max_length=12)
    user_role = models.CharField(max_length=2, choices=UserRole, default=UserRole.CI)
    picture = models.ImageField(upload_to='resident/images',null=True,blank=True)
    zip_code  = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'profile {self.name}'
    



 

    






