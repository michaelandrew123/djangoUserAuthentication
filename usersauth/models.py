from django.db import models

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Employee(models.Model):
    name = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.CharField(max_length=255)
    dob = models.DateField()
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)


class Reporter(models.Model):
    status = models.BooleanField()


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)


class Musician(models.Model):
    instrument = models.CharField(max_length=100)
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    num_stars = models.IntegerField()


