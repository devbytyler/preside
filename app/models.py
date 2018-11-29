import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.utils import timezone

DEFAULT_PROFILE_PICTURE_URL = 'https://s3-us-west-2.amazonaws.com/myroadmap.io/images/profiles/nobody.jpg'


# date_created = models.DateField(default=timezone.now)

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # apartment
    # organization = models.ForeignKey(Organization)
    # status
    # gender
    # picture
    # calling
    # notes

# class User(models.Model):

# class Meeting(models.Model):
#     subject (Person)
#     interviewer (User)
#     notes 
#     date
#     confidential
#     type

# class Organization(models.Model):
#     name
#     parent optional


# class User(AbstractUser):
#     """ This comes from the AbstractUser class
#     id
#     password
#     last_login
#     is_superuser
#     username
#     first_name
#     last_name
#     is_staff
#     is_active
#     date_joined
#     """
#     email = models.EmailField(unique=True)
    # mentors = models.ManyToManyField('User', related_name='+', blank=True, limit_choices_to={'groups__name': 'Mentor'})
    # roadmaps = models.ManyToManyField('Roadmap', related_name='users', blank=True)
    # coach = models.ManyToManyField('self', related_name='students', symmetrical=False, blank=True, limit_choices_to={'groups__name': 'Coach'})
    # These are called groups in the interface
    # cohort = models.ManyToManyField(Cohort, blank=True, related_name='users', help_text='Users should only be in ONE group. Mentor can be in multiple groups.')
    # is_approved = models.BooleanField(default=False, blank=True)
    # phone_number = models.CharField(max_length=15, blank=True)
    # bio = models.TextField(blank=True)
    # resume = models.FileField(upload_to='documents/resumes/', blank=True)
    # photo = models.FileField(upload_to='images/profiles/', blank=True)
    # last_seen = models.DateTimeField(null=True, blank=True)
    # sidebar_list = models.CharField(max_length=500, blank=True, null=True)
    # last_downloaded_competencies = models.DateTimeField(null=True, blank=True)
    # notes_for_coach = models.TextField(blank=True)
    # coach_notes_regarding_student = models.TextField(blank=True)
    # company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)


    # def __str__(self):
    #     return '%s %s' % (self.first_name, self.last_name)

    # @property
    # def is_online(self):
    #     if self.last_seen:
    #         elapsed = now() - self.last_seen
    #         if elapsed < datetime.timedelta(minutes=10):
    #             return True
    #     return False

    # @property
    # def group_names(self):
    #     if self._group_names is None:
    #         self._group_names = set(self.groups.values_list('name', flat=True))
    #     return self._group_names

    # def is_company_admin(self):
    #     return not self.cohort.exists() and 'Admin' in self.group_names

    # def is_cohort_admin(self, cohort=None):
    #     if 'Admin' in self.group_names:
    #         if cohort:
    #             return cohort in self.cohort.all()
    #         else:
    #             return self.cohort.exists()
    #     return False

    # def can_edit_template(self, roadmap=None):
    #     if 'Admin' in self.group_names:
    #         return True
    #         # for cohort in roadmap.cohorts.all():
    #         #     if self.is_cohort_admin(cohort):
    #         #         return True
    #     return False

    # def can_access_user(self, user):
    #     if self == user or self.is_superuser:
    #         return True
    #     elif self.is_admin() and self.company == user.company:
    #         return True
    #     elif self.is_coach() and user.coach.filter(id=self.id).exists():
    #         return True
    #     print("Unauthorized user. Access not granted.")
    #     return False


    # def is_student(self):
    #     return 'User' in self.group_names

    # def is_coach(self):
    #     return 'Coach' in self.group_names

    # def is_admin(self):
    #     return 'Admin' in self.group_names

    # def is_mentor(self):
    #     return 'Mentor' in self.group_names

    # def get_photo_url(self):
    #     return self.photo.url if self.photo else DEFAULT_PROFILE_PICTURE_URL


# pages 
#     all persons
#     drill down person
#     all meetings
#     create meeting
