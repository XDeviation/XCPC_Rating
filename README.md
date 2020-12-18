# XCPC_Ration
一个计算所有XCPC队伍Rating的项目

## 使用说明
- finalrating 就是截至目前所有队伍的 rating
- getrank.py是牛客的爬虫
- 每场比赛的rank数据存在contest下
- 每场比赛之后的rating变化存在change下
- 注意rating变化有先后顺序，详见下面的参考数据
- change 文件夹下是每场比赛的rating变化

## 计算方式：
- 每支队伍初始rating为1500
- 使用Elo积分计算每场比赛后rating变化
- 也就是CodeForces的计算方式

## 参考数据（依照时间顺序）：
- 2020小米ICPC邀请赛预选赛1 ICPC2020XiaomiBefore1
- 2020小米ICPC邀请赛预选赛2 ICPC2020XiaomiBefore2
- 2020小米ICPC邀请赛现场赛 ICPC2020XiaomiFinal
- 2020ICPC上海站 ICPC2020Shanghai

## 注意
- ？！。 的全半角

## TODO
- ccpc.io的爬虫
- 根据当场比赛的所有队伍计算排名（因为没有找到爬每场比赛的参赛队伍的手段）