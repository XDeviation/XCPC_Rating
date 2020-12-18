from __future__ import absolute_import
from typing import List, Dict, Any, Optional
from tinydb import TinyDB, Query
from tinydb.operations import add, decrement, set
import logging
import random
db = TinyDB('data/list.json', indent=4)
teamdata = Query()


def takerank(x):
    return (int)(x[2])


file = 'teams/2020ICPCNanjing'
guessteam = []
f = open(file, 'r')
ranklist = f.read().split('\n')
for team in ranklist:
    data = team.split(' ')
    # print(data)
    l = len(data)
    if l > 5:
        nowteam = db.search((teamdata.chschool == data[1])
                            & (teamdata.chname == data[-4]))
        if len(nowteam) == 0:
            pass
        else:
            i = nowteam[0]
            if i['bestrank'] != 65536:
                guessteam.append((
                    i['chname'],
                    i['chschool'],
                    i['rating'],
                ))
guessteam.sort(key=takerank, reverse=True)
print(file[6:])
print("| Rank | School | Name | Rating |")
print("| ---- | ---- | ---- | ---- |")
rank = 1
for i in guessteam:
    print(f"| {rank} | {i[1]} | {i[0]} | {i[2]} |")
    rank += 1
