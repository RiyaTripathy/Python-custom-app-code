import json
import requests
from datetime import datetime


#enter the API token, url
token = "" 
url= ""


header = {
	"Accept": "application/json",
    'authorization': 'SSWS '+token,
    'content-type': 'application/json'

    }



def process_request(firstname, lastname , email , login , phno , region):
	#data = "{profile:{firstName:"+firstname+" ,lastname":lastname+", email":email, "login":login, "mobilePhone":phno}}
	jsonTosend = {"profile": {"firstName": firstname, "lastName": lastname, "email": email, "login": login}}
	print(jsonTosend)
	res = requests.post(url+'/api/v1/users?activate=false', headers=header, json=jsonTosend)
	if res.status_code == 200:
		print('user created')
	else:
		print('user not created')

	print(res)

	

