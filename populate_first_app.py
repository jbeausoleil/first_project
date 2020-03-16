import os
from django.conf import settings
import django
import random

django.setup() # Fix for Apps not loading

from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()

topic = ['search', 'social', 'market', 'news', 'game']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topic))[0]
    print(t)
    t.save()
    return t


def populate_fake(n=5):
    for entry in range(n):
        top = add_topic()

        # Create the fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webage entry
        webpage = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

        # Create the new access record entry
        acc_record = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]


if __name__ == '__main__':
    print('Populating fake data')
    populate_fake(20)
    print('Populating complete')
