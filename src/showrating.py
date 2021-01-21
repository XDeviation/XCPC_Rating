from __future__ import absolute_import
from typing import List, Dict, Any, Optional
from tinydb import TinyDB, Query
from tinydb.operations import add, decrement, set


def takerank(x):
    return (int)(x[2])


db = TinyDB('data/data.json', indent=4)
teamdata = Query()
now = db.all()
team = []
for i in now:
    team.append((
        i['members'],
        i['chschool'],
        i['rating'],
        i['history'][len(i['history']) - 1]['team_name'],
    ))
print("| Rank | School | Name | Members | Rating |")
print("| ---- | ---- | ---- | ---- | ---- |")
team.sort(key=takerank, reverse=True)
rank = 1
for i in team:
    s = ''
    for name in i[0]:
        s = ' ' + name + s
    print(f"| {rank} | {i[1]} | {i[3]} |{s} | {i[2]} |")
    rank += 1
