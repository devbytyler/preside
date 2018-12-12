import datetime
import random

from django.core.management.base import BaseCommand
from faker import Faker

from app.models import Person, Organization, User, Meeting

class Command(BaseCommand):
    help = 'Seed the datas'

    def handle(self, *args, **options):
        fake = Faker()
        
        org = Organization.objects.create(name="152 Ward")

        super_user = User.objects.create_superuser('super', 'super@preside.com', '123', first_name="super", last_name="user", organization=org)
        normal_user = User.objects.create_user(
            username='user',
            email='tylerstephens814@gmail.com',
            password='123',
            first_name='Tyler',
            last_name='Stephens',
            organization=org,
        )

        other_user = User.objects.create_user(
            username='user2',
            email='user2@preside.com',
            password='123',
            first_name='Mike',
            last_name='Jones',
            organization=org,
        )

        people = []
        meetings = []
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
            person = Person(
                first_name=name,
                last_name=fake.last_name(),
                apartment=random.randint(1,24),
                organization=org,
                gender=gender,
                photo_url=photo_url,
                notes=fake.paragraph() + ' ' + fake.paragraph()
            )
            people.append(person)
        Person.objects.bulk_create(people)
        
        for i in range(50):
            rand_int = random.randint(1,30)
            par = fake.paragraph() + ' ' + fake.paragraph()
            meetings.append(Meeting(
                user=normal_user,
                person_id=rand_int,
                notes=par,
            ))

        for i in range(50):
            rand_int = random.randint(1,30)
            par = fake.paragraph() + ' ' + fake.paragraph()
            meetings.append(Meeting(
                user=other_user,
                person_id=rand_int,
                notes=par,
            ))        

        Meeting.objects.bulk_create(meetings)

