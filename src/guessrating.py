from __future__ import absolute_import
from typing import List, Dict, Any, Optional
from tinydb import TinyDB, Query
from tinydb.operations import add, decrement, set
from itertools import chain
from pypinyin import pinyin, Style
import logging
import random
db = TinyDB('../data/data.json', indent=4)
teamdata = Query()


def takerank(x):
    return (int)(x[2])


def to_pinyin(s):
    return ''.join(chain.from_iterable(pinyin(s, style=Style.TONE3)))


file = '../guess/CCPC2021Xiangtan'
guessteam = []
noincteam = []
f = open(file, 'r')
ranklist = f.read().split('\n')
for team in ranklist:
    data = team.split(' ')
    if len(data) > 1:
        members = data[3:6]
        members.sort(key=to_pinyin)
        # print(members)
        if '*' in data:
            data[1] = '☆' + data[1]
        nowteam = db.search(teamdata.members.all(members))
        if len(nowteam) == 0:
            noincteam.append(data[1:6])
        else:
            # print(nowteam[0])
            i = nowteam[0]
            guessteam.append((
                data[2],
                data[1],
                i['rating'],
            ))
guessteam.sort(key=takerank, reverse=True)
print("CCPC2021Xiangtan Included")
print("| Rank | School | Name | Rating |")
print("| ---- | ---- | ---- | ---- |")
rank = 1
for i in guessteam:
    print(f"| {rank} | {i[1]} | {i[0]} | {i[2]} |")
    rank += 1
print("CCPC2021Xiangtan Not Included")
print("| School | Name |")
for i in noincteam:
    print(f"| {i[0]} | {i[1]} |")
# print(data)
# l = len(data)
# if l > 5:
#     teamname = ''
#     for i in range(2, l - 6):
#         teamname = teamname + data[i]
#     if teamname[0] == '☆':
#         teamname = teamname[1:]
#     nowteam = db.search((teamdata.chschool == data[1])
#                         & (teamdata.chname == teamname))
#     if len(nowteam) == 0:
#         pass
#     else:
#         i = nowteam[0]
#         if i['bestrank'] != 65536:
#             guessteam.append((
#                 i['chname'],
#                 i['chschool'],
#                 i['rating'],
#             ))
# guessteam.sort(key=takerank, reverse=True)
# print(file[6:])
# print("| Rank | School | Name | Rating |")
# print("| ---- | ---- | ---- | ---- |")
# rank = 1
# for i in guessteam:
#     print(f"| {rank} | {i[1]} | {i[0]} | {i[2]} |")
#     rank += 1
