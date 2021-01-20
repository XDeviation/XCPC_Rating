from __future__ import absolute_import
from typing import List, Dict, Any, Optional
from tinydb import TinyDB, Query
from tinydb.operations import add, decrement, set
db = TinyDB('../data/list.json', indent=4)
teamdata = Query()
s = input()
nowteam = db.search((teamdata.chschool == s) | (teamdata.chname == s))
if len(nowteam) > 0:
    for i in nowteam:
        print(i)