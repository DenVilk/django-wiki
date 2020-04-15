import requests
import json
import time
from codeforces import CodeforcesAPI
from codeforces import ProblemResult
from codeforces import Problem
from codeforces import ProblemStatistics
from codeforces import ProblemType

bank_url = "https://nbrb.by/API/ExRates/Rates/"
cf_url = 'https://codeforces.com/api/'

def Currency(cid):
    req = bank_url + str(cid)
    r = requests.get(req)
    print(req)
    value = str(int(r.json()['Cur_OfficialRate']*100)/100)
    scale = str(r.json()['Cur_Scale'])
    return {'value': value, 'scale': scale}

def Contests():
    api = CodeforcesAPI()
    url = 'http://codeforces.com/contest/{}'
    answer = ""
    url_registration = 'http://codeforces.com/contestRegistration/{}'
    x = api.contest_list(False)
    answer = []
    for c in x:
        if (c.start_time > int(time.time())):
            answer.append({'name':c.name, 'date': time.ctime(c.start_time)})
    return answer