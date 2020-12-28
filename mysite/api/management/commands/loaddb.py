from django.core.management.base import BaseCommand, CommandError
from api.models import *
from openpyxl import load_workbook 


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
        print(f'count = {count}')
        #row4 = [ ws[f'{c}4'].value for c in 'ABCDEFG' ]
        #print( row4 )
        for i in range(count): # 0,1,2,3
            w = Work(**{
                    # 'id': int(ws[f'A{4+i}'].value),
                    'lat': float(ws[f'B{4+i}'].value),
                    'lng': float(ws[f'C{4+i}'].value),
                    'date': str(ws[f'D{4+i}'].value),
                    'area': float(ws[f'E{4+i}'].value),
                    # 'rice_type': str(ws[f'F{4+i}'].value),
                    'other': str(ws[f'G{4+i}'].value),
                    'RepairTime': str(ws[f'H{4+i}'].value),
                    'Harverstime': str(ws[f'I{4+i}'].value),
                    'money': str(ws[f'J{4+i}'].value),
                    # 'moneyStatus': str(ws[f'K{4+i}'].value),
                    # 'work_status ': str(ws[f'L{4+i}'].value),
                    
                })
            w.save()


     
            # f = Farmer(**{
            #         'id': int(ws[f'A{4+i}'].value),
            #         'farmer_name': str(ws[f'B{4+i}'].value),
            #         'phone': str(ws[f'C{4+i}'].value),
            #         'address': str(ws[f'D{4+i}'].value),
            #         'email': str(ws[f'E{4+i}'].value),
            #         'username': str(ws[f'F{4+i}'].value),
            #         'password': str(ws[f'G{4+i}'].value),
                    
            #     })
            # f.save()

    
            # r = Owner(**{
            #     #    'id': int(ws[f'A{4+i}'].value),
            #         'owner_name': str(ws[f'B{4+i}'].value),
            #         'phone': str(ws[f'C{4+i}'].value),
            #         'address': str(ws[f'D{4+i}'].value),
            #         'email': str(ws[f'E{4+i}'].value),
            #         'username': str(ws[f'F{4+i}'].value),
            #         'password': str(ws[f'G{4+i}'].value),
                    
            #     })
            # r.save()
        #     w = Work(**{
        #             'id': int(ws[f'A{4+i}'].value),
        #             'lat': float(ws[f'B{4+i}'].value),
        #             'lng': float(ws[f'C{4+i}'].value),
        #             'date': str(ws[f'D{4+i}'].value),
        #             'area': float(ws[f'E{4+i}'].value),
        #             # 'rice_type': str(ws[f'F{4+i}'].value),
        #             'other': str(ws[f'G{4+i}'].value),
        #             'RepairTime': str(ws[f'H{4+i}'].value),
        #             'Harverstime': str(ws[f'I{4+i}'].value),
        #             'money': str(ws[f'J{4+i}'].value),
        #             # 'moneyStatus': str(ws[f'K{4+i}'].value),
        #             # 'work_status ': str(ws[f'L{4+i}'].value),
                    
        #         })
        # w.save()

    
            # t = Rice_type(**{
            #         # 'id': int(ws[f'A{4+i}'].value),
            #         'rice_type': str(ws[f'B{4+i}'].value),
                   
                    
                    
            #     })
            # t.save()

            # t = Tractor(**{
            #         # 'id': int(ws[f'A{4+i}'].value),
            #         'tractor': str(ws[f'B{4+i}'].value),
                   
                    
                    
            #     })
            # t.save()


            # t = Work_status(**{
            #         # 'id': int(ws[f'A{4+i}'].value),
            #         'work_status': str(ws[f'B{4+i}'].value),
                   
                    
                    
            #     })
            # t.save()

            # t = Money_status(**{
            #         # 'id': int(ws[f'A{4+i}'].value),
            #         'moneyStatus': str(ws[f'B{4+i}'].value),
                   
                    
                    
            #     })
            # t.save()

