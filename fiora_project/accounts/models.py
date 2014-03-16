from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('F','Lady'),
        ('M','Gentleman'),
        ('R','Robot'),
    )
    WEAPON_CHOICES = (
        ('B', 'Blade Wielding'),
        ('G', 'Gun Slinging'),
        ('F', 'Fist Pounding'),
        ('R', 'Rhyme Spitting'),
    )
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weapon = models.CharField(max_length=1, choices=WEAPON_CHOICES)
    is_active = models.BooleanField(default=False)