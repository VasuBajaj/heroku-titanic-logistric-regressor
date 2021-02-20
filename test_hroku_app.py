# heroku url
import requests
import json

heroku_url = 'https://titanic-flask-app2.herokuapp.com/' # change to your app name
# sample data
data = {  'Pclass': 3
             , 'Age': 2
             , 'SibSp': 1
             , 'Fare': 50}
data = json.dumps(data)

send_request = requests.post(heroku_url, data)
print(send_request)

print(send_request.json())