from django.core.management.base import BaseCommand, CommandError
from api.models import queue

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        #parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        # pass
        from openpyxl import load_workbook
        filename = "xlsx/แผนการดำเนินโครงงานที่ปรึกษา senior project 62 - เกษ.xlsx"
        wb = load_workbook(filename, data_only=True)
        ws = wb['Data']
        count = int(ws['A2'].value)
        print(f'queue count = {count}')
        #row4 = [ ws[f'{c}4'].value for c in 'ABCDEFG' ]
        #print( row4 )
        for i in range(count): # 0,1,2,3
            q = queue(**{
                    'id': int(ws[f'A{4+i}'].value),
                    'lat': float(ws[f'B{4+i}'].value),
                    'lng': 104.903
                })
        q.save()

3
