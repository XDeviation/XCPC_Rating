from __future__ import absolute_import
from typing import List, Dict, Any, Optional
from tinydb import TinyDB, Query
from tinydb.operations import add, decrement, set
import json
import logging
import random
from itertools import chain
from pypinyin import pinyin, Style


def to_pinyin(s):
    return ''.join(chain.from_iterable(pinyin(s, style=Style.TONE3)))


db = TinyDB('../data/data.json', indent=4)
teamdata = Query()
f = open('../data/CCPC2020Changchun.json', 'r')
ranklist = f.read()
text = json.loads(ranklist)
for team in text:
    members = team['members']
    members.sort(key=to_pinyin)
    # print(members)
    nowteam = db.search(teamdata.members.all(members))
    nowrank = {
        'contest_name': 'CCPC2020Changchun',
        'team_name': team['name'],
        'rank': team['place']['all'],
    }
    if len(nowteam) == 0:
        db.insert({
            'chschool': f"{team['organization']}",
            'enschool': "",
            'rating': 1500,
            'members': members,
            'history': [nowrank],
            'bestrank': (int)(team['place']['all']),
        })
    else:
        print(nowteam[0])
