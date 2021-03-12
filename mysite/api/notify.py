import requests

url = 'https://notify-api.line.me/api/notify'
token = 'xjcBMfMHxrj0NuJzLL2INZmRNB7r6RClVdcFucX9hS2'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

msg = '555555'
r = requests.post(url, headers=headers, data = {'message':msg})
print r.text