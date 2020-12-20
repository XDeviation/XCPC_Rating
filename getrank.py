import requests
import time
import json
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}


def nowcoder(url, pages=1) -> None:
    for page in range(pages):
        params = {
            'page': page + 1,
        }
        res = requests.get(url, headers=headers, params=params)
        data = res.json()
        for i in data['data']['rankData']:
            name = i['userName']
            school = '----'
            if 'school' in i:
                school = i['school']
            rank = i['ranking']
            if '☆' in name:
                name = name[1:]
            print(f"{name}\t{school}\t{rank}")
        time.sleep(1)


if __name__ == "__main__":
    url = ''  #在每场比赛榜单的 Network XHR 下面
    nowcoder(url, 1)  # pages 指榜单页数
