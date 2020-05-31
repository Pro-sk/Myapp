from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30,verbose_name='Username')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=10,verbose_name='Mobile No')
    # GENDER_MALE = 0
    # GENDER_FEMALE = 1
    GENDER_CHOICES = [(0, 'Male'), (1, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    def __str__(self):
        return self.name
