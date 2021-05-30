from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_head = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    email = models.CharField(max_length=254)

    def __str__(self):
        return self.user.username


class EventRegistration(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    college_name = models.CharField(max_length=254)
    event_name = models.CharField(max_length=254)


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')


class valorant_registration(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    college_name = models.CharField(max_length=254)
    dicord_id = models.CharField(max_length=254)
    valorant_id = models.CharField(max_length=254)
    student_id = models.ImageField(upload_to='images/')


class csgo_registration(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    college_name = models.CharField(max_length=254)
    dicord_id = models.CharField(max_length=254)
    csgo_id = models.CharField(max_length=254)
    student_id = models.ImageField(upload_to='images/')


class clash_registration(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    college_name = models.CharField(max_length=254)
    dicord_id = models.CharField(max_length=254)
    player_id = models.CharField(max_length=254)
    student_id = models.ImageField(upload_to='images/')


class callofduty_registration(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    college_name = models.CharField(max_length=254)
    dicord_id = models.CharField(max_length=254)
    player_id = models.CharField(max_length=254)
    student_id = models.ImageField(upload_to='images/')


class amongus_registration(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    college_name = models.CharField(max_length=254)
    dicord_id = models.CharField(max_length=254)
    player_id = models.CharField(max_length=254)
    student_id = models.ImageField(upload_to='images/')


class treasurehunt_registration(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    college_name = models.CharField(max_length=254)
    dicord_id = models.CharField(max_length=254)
    insta_id = models.CharField(max_length=254)
    student_id = models.ImageField(upload_to='images/')

#  Pre tech fest Models


class scrib_registration(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    college_name = models.CharField(max_length=254)
    dicord_id = models.CharField(max_length=254)
    student_id = models.ImageField(upload_to='images/')


class bolly_registration(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    college_name = models.CharField(max_length=254)
    dicord_id = models.CharField(max_length=254)
    student_id = models.ImageField(upload_to='images/')


class meme_registration(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    college_name = models.CharField(max_length=254)
    dicord_id = models.CharField(max_length=254)
    insta_id = models.CharField(max_length=254)
    student_id = models.ImageField(upload_to='images/')
    meme_upload = models.ImageField(upload_to='images/memes/')


class chess_registration(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    college_name = models.CharField(max_length=254)
    dicord_id = models.CharField(max_length=254)
    chess_id = models.CharField(max_length=254)
    student_id = models.ImageField(upload_to='images/')


class openmic_registration(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    college_name = models.CharField(max_length=254)
    dicord_id = models.CharField(max_length=254)
    student_id = models.ImageField(upload_to='images/')


class bug_registration(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    branch = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    college_name = models.CharField(max_length=254)
    dicord_id = models.CharField(max_length=254)
    student_id = models.ImageField(upload_to='images/')
