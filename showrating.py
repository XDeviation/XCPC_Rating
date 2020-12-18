from __future__ import absolute_import
from typing import List, Dict, Any, Optional
from tinydb import TinyDB, Query
from tinydb.operations import add, decrement, set


def takerank(x):
    return (int)(x[1])


db = TinyDB('data/list.json', indent=4)
teamdata = Query()
now = db.all()
team = []
for i in now:
    team.append((
        i['chname'],
        i['rating'],
    ))
team.sort(key=takerank, reverse=True)
for i in team:
    print(f"{i[0]} {i[1]}")