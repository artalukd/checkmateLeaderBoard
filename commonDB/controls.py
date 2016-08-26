import requests
'''import time
from .models import PlayerProfile

def leaderboard():
    ip = ['172.17.44.83:8000',]
    while(True):
        l = []
        for i in ip:
            re = requests.get('http://'+ i +'/pokemon/send_all')
            if re.status_code = 200
                d = re.json()
                l += d['players']
        pushToDb(l)
        sortDB()
        time.sleep(40)

def sortDB():
    pp = PlayerProfile.objects.all()
    pp = sorted(pp, key= lambda PlayerProfile: PlayerProfile.pokemoney , reverse=True)
    c = 1
    for i in range(len(pp)):
        i.rank = c
        c++


def pushToDb(lst):

    for p in lst:
        key = str(p['teamname'])+str(p['server'])
        try:
            pp = PlayerProfile.objects.get( index = key )
            pp.pokemoney = p['pokemoney']
        except:
            pp = PlayerProfile( index = key)
            pp.name2 = p['name2']
            pp.name1 = p['name1']
            pp.teamname = p['teamname']
            pp.pokemoney = p['pokemoney']
'''
