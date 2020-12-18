from __future__ import absolute_import
from typing import List, Dict, Any, Optional
from tinydb import TinyDB, Query
from tinydb.operations import add, decrement, set
import logging
import random
db = TinyDB('data/list.json', indent=4)
teamdata = Query()

file = 'teams/2020ICPCNanjing'
f = open(file, 'r')
ranklist = f.read().split('\n')
for team in ranklist:
    data = team.split(' ')
    # print(data)
    l = len(data)
    if l > 5:
        en = ''
        for i in range(2, l - 4):
            en = en + data[i] + ' '
        en = en[0:len(en) - 1]
        nowteam = db.search((teamdata.chschool == data[1])
                            & (teamdata.chname == data[-4]))
        if len(nowteam) == 0:
            db.insert({
                'chname': f"{data[-4]}",
                'enname': f"{en}",
                'chschool': f"{data[1]}",
                'enschool': "",
                'rating': 1500,
                'members': [
                    data[-3],
                    data[-2],
                    data[-1],
                ],
                'history': [],
                'bestrank': 65536,
            })
            print(data[1], en, data[-4], data[-3], data[-2], data[-1])
        else:
            db.update(
                add('members', [
                    data[-3],
                    data[-2],
                    data[-1],
                ]),
                (teamdata.chschool == data[1]) & (teamdata.chname == data[-4]),
            )
            db.update(
                set('enname', en),
                (teamdata.chschool == data[1]) & (teamdata.chname == data[-4]),
            )
