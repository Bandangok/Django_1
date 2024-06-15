import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone
from django.conf import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(settings.PHONES_CSV, 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        # for phone in phones:
        #     # TODO: Добавьте сохранение модели
        #     Phone.objects.create(
        #         id=phone['id'],
        #         name=phone['name'],
        #         price=phone['price'],
        #         image=phone['image'],
        #         release_date=phone['release_date'],
        #         lte_exists=phone['lte_exists'],
        #         slug=slugify(phone['name'])
        #     )

        for phone in phones:
            # TODO: Добавьте сохранение модели
            phone = Phone(
                id=phone['id'],
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=slugify(phone['name'])
            )
            phone.save()
        pass