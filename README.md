# XCPC_Ration
一个计算所有XCPC队伍Rating的项目

## 使用说明
- finalrating 就是截至目前所有队伍的 rating
- getrank.py是牛客的爬虫
- 每场比赛的rank数据存在contest下
- 每场比赛之后的rating变化存在change下
- 注意rating变化有先后顺序，详见下面的参考数据

## 计算方式：
- 每支队伍初始rating为1500
- 使用Elo积分计算每场比赛后rating变化
- 也就是CodeForces的计算方式

## 参考数据（依照时间顺序）：
- ICPC2020Xiaomi
- ICPC2020ShangHai

## TODO
ccpc.io的爬虫
根据当场比赛的所有队伍计算排名（因为没有找到爬每场比赛的参赛队伍的手段）