# XCPC_Rating
一个计算所有XCPC队伍Rating的项目

## 使用说明
- finalrating 就是截至目前所有队伍的 rating
- getrank.py 是牛客的爬虫
- 每场比赛的 rank 数据存在 contest 下
- 每场比赛之后的 rating 变化存在 change 下
- 注意 rating 变化有先后顺序，详见下面的参考数据
- change 文件夹下是每场比赛的rating变化

## 计算方式：
- 每支队伍初始rating为1500
- 使用Elo积分计算每场比赛后rating变化
- 也就是CodeForces的计算方式

## 参考数据（依照时间顺序）：
- 2020CCPC女生专场 CCPC2020Girl
- 2020CCPC秦皇岛站 CCPC2020Qinghuangdao
- 2020CCPC威海站 CCPC2020Weihai
- 2020CCPC绵阳站 CCPC2020Mianyang
- 2020CCPC长春站 CCPC2020Changchun
- 2020ICPC上海站 ICPC2020Shanghai
- 2020ICPC南京站 ICPC2020Nanjing
- 2020ICPC济南站 ICPC2020Jinan

## TODO
- ~~ccpc.io的爬虫~~

## 声明
- 所有数据（队伍排名，比赛赛况，参赛选手等）均来源于网络公开数据，如若侵犯个人隐私请直接提issue，会尽快处理。
