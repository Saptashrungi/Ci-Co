from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from datetime import datetime


class Person(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    checkin_time = models.DateTimeField(null=True, blank=True)
    checkout_time = models.DateTimeField(null=True, blank=True)
    phone_no = models.CharField(max_length=10, unique=True)
    details = models.CharField(max_length=150, null=True, blank=True)
    is_authenticated = models.BooleanField(default=False)

    def checkin(self):
        self.checkin_time = datetime.now()
        self.save()

    def checkout(self):
        self.checkout_time = datetime.now()
        self.save()

    def verify(self, username, password):
        if(self.username == username and self.password == password):
            self.is_authenticated=True
            self.save()
            return self
        return None

    def __str__(self):
        return self.username
