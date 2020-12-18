from __future__ import absolute_import
from typing import List, Dict, Any, Optional
from tinydb import TinyDB, Query
from tinydb.operations import add, decrement, set
import json
import sys
import math


class User():
    def __init__(self, rank, old_rating, handle='', official_new_rating=0):
        self.rank = float(rank)
        self.old_rating = int(old_rating)
        self.seed = 1.0
        self.handle = str(handle)
        # official_new_rating: used for validating result
        self.official_new_rating = int(official_new_rating)


class RatingCalculator():
    def __init__(self):
        self.user_list = []

    def cal_p(self, user_a, user_b):
        return 1.0 / (1.0 +
                      pow(10, (user_b.old_rating - user_a.old_rating) / 400.0))

    def get_ex_seed(self, user_list, rating, own_user):
        ex_user = User(0.0, rating)
        result = 1.0
        for user in user_list:
            if user != own_user:
                result += self.cal_p(user, ex_user)
        return result

    def cal_rating(self, user_list, rank, user):
        left = 1
        right = 8000
        while right - left > 1:
            mid = int((left + right) / 2)
            if self.get_ex_seed(user_list, mid, user) < rank:
                right = mid
            else:
                left = mid
        return left

    def calculate(self):
        # Calculate seed
        for i in range(len(self.user_list)):
            self.user_list[i].seed = 1.0
            for j in range(len(self.user_list)):
                if i != j:
                    self.user_list[i].seed += self.cal_p(
                        self.user_list[j], self.user_list[i])
            # print(self.user_list[i].seed)
        # Calculate initial delta and sum_delta
        sum_delta = 0
        for user in self.user_list:
            user.delta = int(
                (self.cal_rating(self.user_list,
                                 math.sqrt(user.rank * user.seed), user) -
                 user.old_rating) / 2)
            sum_delta += user.delta
        # Calculate first inc
        inc = int(-sum_delta / len(self.user_list)) - 1
        for user in self.user_list:
            user.delta += inc
            # print(user.delta)
        # Calculate second inc
        self.user_list = sorted(self.user_list,
                                key=lambda x: x.old_rating,
                                reverse=True)
        s = min(len(self.user_list),
                int(4 * round(math.sqrt(len(self.user_list)))))
        sum_s = 0
        for i in range(s):
            sum_s += self.user_list[i].delta
        inc = min(max(int(-sum_s / s), -10), 0)
        # Calculate new rating
        for user in self.user_list:
            user.delta += inc
            user.new_rating = user.old_rating + user.delta
            # print(user.new_rating)
        self.user_list = sorted(self.user_list,
                                key=lambda x: x.rank,
                                reverse=False)


db = TinyDB('data/list.json', indent=4)
teamdata = Query()
file = input()
f = open(file, 'r')
ranklist = f.read().split('\n')
# print(ranklist)
calculator = RatingCalculator()
last_idx = 0
last_rank = 1
for team in ranklist:
    if team == '':
        pass
    else:
        teamlist = team.split('\t')
        # print(teamlist)
        teamindb = db.search((teamdata.chname == teamlist[0])
                             & (teamdata.chschool == teamlist[1]))
        if len(teamindb) == 0:
            db.insert({
                'chname': f"{teamlist[0]}",
                'enname': "",
                'chschool': f"{teamlist[1]}",
                'enschool': "",
                'rating': 1500,
                'members': [],
                'history': [],
                'bestrank': (int)(teamlist[2]),
            })
            calculator.user_list.append(
                User(
                    rank=teamlist[2],
                    old_rating=1500,
                    handle=teamlist[0],
                ))
        else:
            nowteam = teamindb[0]
            # print(nowteam)
            if (int)(teamlist[2]) < nowteam['bestrank']:
                db.update(
                    set('bestrank', (int)(teamlist[2])),
                    (teamdata.chname == teamlist[0])
                    & (teamdata.chschool == teamlist[1]),
                )
            calculator.user_list.append(
                User(
                    rank=teamlist[2],
                    old_rating=nowteam['rating'],
                    handle=teamlist[0],
                ))

calculator.calculate()
for i in range(len(ranklist) - 1):
    teamlist = ranklist[i].split('\t')
    nowteam = calculator.user_list[i]
    db.update(
        set('rating', nowteam.new_rating),
        (teamdata.chname == teamlist[0])
        & (teamdata.chschool == teamlist[1]),
    )
    db.update(
        add('history', [f"{file}"]),
        (teamdata.chname == teamlist[0])
        & (teamdata.chschool == teamlist[1]),
    )
    print(f"{nowteam.handle} {nowteam.old_rating} -> {nowteam.new_rating}")
