import requests

url = 'https://notify-api.line.me/api/notify'
            token = 'yrpItRRDCVa9eiFSOXexHi3vXcxp9VBJpu9i2xTSaPP'
            headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
            print(req.POST)
            form = FarmerWorkForm(req.POST)
            if form.is_valid():
                work = Work()
                work.farmer_name = req.user
                work.area = req.POST['area']
                work.rice_type = Rice_type.objects.get(pk=req.POST['rice_type'])
                work.rice = req.POST['rice']
                work.workDetail = req.POST['workDetail']
                msg = "จองคิวแล้ว"
                r = requests.post(url, headers=headers, data = {'message':msg})
                work.save()
            return redirect('/addWork')