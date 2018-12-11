import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.utils import timezone

DEFAULT_PROFILE_PICTURE_URL = 'https://s3-us-west-2.amazonaws.com/myroadmap.io/images/profiles/nobody.jpg'

# date_created = models.DateField(default=timezone.now)

class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Person(models.Model):
    RED = 'RED'
    YELLOW = 'YELLOW'
    GREEN = 'GREEN'
    UNKNOWN = 'UNKNOWN'
    M = 'MALE'
    F = 'FEMALE'

    STATUS_OPTIONS = (
        (RED, 'Red'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (UNKNOWN, 'Unknown'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    apartment = models.IntegerField(blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_OPTIONS,
        default=UNKNOWN,
    )
    gender = models.CharField(
        max_length=20,
        choices=((M, 'Male'), (F, 'Female')),
        default=None
    )
    calling = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    photo_url = models.CharField(max_length=255, default=DEFAULT_PROFILE_PICTURE_URL)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class User(AbstractUser):
    """ This comes from the AbstractUser class
    id
    password
    last_login
    is_superuser
    username
    first_name
    last_name
    email
    is_staff
    is_active
    date_joined
    """

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_full_name}"

class Meeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    person = models.ForeignKey(Person, related_name="meetings", on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    confidential = models.BooleanField(default=True)
    notes = models.TextField()
