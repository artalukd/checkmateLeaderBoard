from django.shortcuts import render
import requests
import json
from django.http import HttpResponse

playerlst=[]
def refresh(request):
    ip = ['172.17.44.83:8000']
    if request.method == 'GET' :
        plst = []
        print(1)
        for i in ip:
            print(2)
            re = requests.get('http://'+ i +'/pokemon/send_all',timeout = (3,5))
            if re.status_code == 200:
                d = re.json()
                plst += d['players']
        playerlst = sorted(plst, key= lambda PlayerProfile: PlayerProfile['pokemoney'] , reverse=True)
        print(playerlst)
    return HttpResponse(json.dumps(playerlst), content_type = "application/json")

def getData(request):
    if request.method == 'GET' :
	       return HttpResponse(json.dumps(playerlst), content_type = "application/json")
