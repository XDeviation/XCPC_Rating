from __future__ import absolute_import
from typing import List, Dict, Any, Optional
from tinydb import TinyDB, Query
from tinydb.operations import add, decrement, set
import logging
import random
db = TinyDB('../data/list.json', indent=4)
teamdata = Query()

file = 'teams/ICPC2020Jinan'
f = open(file, 'r')
ranklist = f.read().split('\n')
for team in ranklist:
    data = team.split(' ')
    # print(data)
    l = len(data)
    if l > 5:
        teamname = ''
        for i in range(2, l - 6):
            teamname = teamname + data[i]
        if teamname[0] == '☆':
            teamname = teamname[1:]
        # print(data[1], teamname, data[-6], data[-4], data[-2])
        membername = [data[-6], data[-4], data[-2]]
        nowteam = db.search((teamdata.members.all(membername)))
        if len(nowteam) >= 1:
            for tmp in nowteam:
                if teamname != tmp['chname']:
                    print(data[1], teamname, data[-6], data[-4], data[-2],
                          tmp['chname'])
