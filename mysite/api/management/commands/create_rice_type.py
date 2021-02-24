from django.core.management.base import BaseCommand, CommandError
from api.models import *
from openpyxl import load_workbook 


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        #parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        t1 = Rice_type()
        t1.rice_type = 'ตั้งตรง'
        t1.save()

        t1 = Rice_type()
        t1.rice_type = 'ราบกับพื้น'
        t1.save()

        t1 = Rice_type()
        t1.rice_type = 'ล้ม'
        t1.save()
