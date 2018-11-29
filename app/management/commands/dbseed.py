import datetime
import random

from django.core.management.base import BaseCommand
from faker import Faker

from app.models import Person

class Command(BaseCommand):
    help = 'Seed the datas'

    def handle(self, *args, **options):
        fake = Faker()

        for x in range(0, 20):
            print(x)
       

