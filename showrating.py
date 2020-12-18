from __future__ import absolute_import
from typing import List, Dict, Any, Optional
from tinydb import TinyDB, Query
from tinydb.operations import add, decrement, set


def takerank(x):
    return (int)(x[2])


db = TinyDB('data/list.json', indent=4)
teamdata = Query()
now = db.all()
team = []
for i in now:
    team.append((
        i['chname'],
        i['chschool'],
        i['rating'],
    ))
print("| Rank | School | Name | Rating |")
print("| ---- | ---- | ---- | ---- |")
team.sort(key=takerank, reverse=True)
rank = 1
for i in team:
    print(f"| {rank} | {i[1]} | {i[0]} | {i[2]} |")
    rank += 1
