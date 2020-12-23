from __future__ import absolute_import
from typing import List, Dict, Any, Optional
from tinydb import TinyDB, Query
from tinydb.operations import add, decrement, set
import logging
import random
db = TinyDB('data/list.json', indent=4)
teamdata = Query()

file = 'teams/2020ICPCJinan'
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

        nowteam = db.search((teamdata.chschool == data[1])
                            & (teamdata.chname == teamname))
        if len(nowteam) == 0:
            db.insert({
                'chname': f"{teamname}",
                'enname': f"",
                'chschool': f"{data[1]}",
                'enschool': "",
                'rating': 1500,
                'members': [
                    data[-6],
                    data[-4],
                    data[-2],
                ],
                'history': [],
                'bestrank': 65536,
            })
            # print(data[1], en, data[-4], data[-3], data[-2], data[-1])
            print(data[1], teamname, data[-6], data[-4], data[-2])

        else:
            db.update(
                set('members', [
                    data[-6],
                    data[-4],
                    data[-2],
                ]),
                (teamdata.chschool == data[1]) & (teamdata.chname == teamname),
            )
