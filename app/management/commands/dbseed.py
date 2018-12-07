import datetime
import random

from django.core.management.base import BaseCommand
from faker import Faker

from app.models import Person, Organization

class Command(BaseCommand):
    help = 'Seed the datas'

    def handle(self, *args, **options):
        fake = Faker()

        org = Organization.objects.create(name="152 Ward")
            
        people = []
        for i in range(30):
            index = random.randint(1,99)
            gender = random.choice([Person.M, Person.F])
            if gender == Person.F:
                photo_gender = 'women'
                name = fake.first_name_female()
            else:
                photo_gender = 'men'
                name = fake.first_name_male()

            photo_url=f"https://randomuser.me/api/portraits/{photo_gender}/{index}.jpg"
            people.append(Person(
                first_name=name,
                last_name=fake.last_name(),
                apartment=random.randint(1,24),
                organization=org,
                gender=gender,
                photo_url=photo_url
            ))
        Person.objects.bulk_create(people)    
       

