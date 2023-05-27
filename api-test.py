import requests 
import json 

url = 'http://127.0.0.1:8000/send-bulk-email/'
headers ={
    'Content-type' : 'application/json; charset=utf8'
}
data = json.dumps({
    'subject':'No-Subject',
    'message':'No-Message'
})
response = requests.post(url, headers=headers, data=data)

print(response)

