# -*- coding:utf-8 -*-
import json
import requests
import bs4
import schedule
import time
import kakaokey

games_info = {
    'pubg': {'url': 'https://www.pubg.com/category/patch-notes-en-gb/', 'source': ''},
    'r6' : {'url':'https://www.ubisoft.com/en-us/game/rainbow-six/siege/news-updates', 'source':''},
    'lol' : {'url':'https://na.leagueoflegends.com/en-us/news/game-updates/', 'source':''}
}


app_key = kakaokey.app_key
redirect_url = kakaokey.redirect_url
temp_key = kakaokey.temp_key

# 인증코드 받아오기
oauth_url = 'https://kauth.kakao.com/oauth/authorize?client_id=' + app_key + '&redirect_uri=' + redirect_url + '&response_type=code'

access_token = kakaokey.access_token
refresh_token = kakaokey.refresh_token


# 메시지 전송 추가 인증
# print('https://kauth.kakao.com/oauth/authorize?client_id='+app_key+'&redirect_uri='+redirect_url+'&response_type=code&scope=talk_message')

def get_token():
    # 인증코드로 토큰 값 받아오기
    req_url = 'https://kauth.kakao.com/oauth/token'
    data = {'grant_type': 'authorization_code', 'client_id': app_key, 'redirect_uri': redirect_url, 'code': temp_key}
    req = requests.post(req_url, data=data)
    # json 내 token, refresh_token 값
    return req.json()


def renew_token():
    # 리프레시 토큰으로 갱신하기
    req_url = 'https://kauth.kakao.com/oauth/token'
    data = {'grant_type': 'refresh_token', 'client_id': app_key, 'refresh_token': refresh_token}
    req = requests.post(req_url, data=data)
    # json 내 token, refresh_token 값
    return req.json()


def make_message(text):
    temp = {
        'object_type': 'text',
        'text': text,
        'link': {
            #                 'web_url': ''
            #                 'mobile_web_url': ''
        },
        'button_title': '바로 확인',

    }
    return {"template_object": json.dumps(temp)}


def send_message(text):
    req_url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
    req_header = {"Content-Type": "application/json", "Content-Type": "x-www-form-urlencoded",
                  "Authorization": 'Bearer ' + access_token}
    req = requests.post(req_url, headers=req_header, params=make_message(text))
    if req.status_code == 200:
        print('success')
    else:
        print(req.text)

def get_source(url):
    h = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    request_result = requests.get(url, headers = h)
    game = request_result.text
    soup = bs4.BeautifulSoup(game, 'html.parser')
    return soup

def date_check(filename, wr, date=''):
    f = open(filename, wr)
    if wr == 'w':
        f.write(date)
        temp = 'success'
    else:
        temp = f.read()
    f.close()
    return temp

def get_pubg(source):
    new_date = source.find('span',class_='c-white').text
    old_date = date_check('pubg.txt', 'r')
    if old_date == new_date:
        return False
    else:
        date_check('pubg.txt', 'w', new_date)
        return True

def get_lol(source):
    new_date = source.find('h2',class_='style__Title-i44rc3-8 jprNto').text
    old_date = date_check('lol.txt', 'r')
    if old_date == new_date:
        return False
    else:
        date_check('lol.txt', 'w', new_date)
        return True

def get_r6(source):
    new_date = source.find('span',class_='date__day').text
    old_date = date_check('r6.txt', 'r')
    if old_date == new_date:
        return False
    else:
        date_check('r6.txt', 'w', new_date)
        return True

def job():
    for i in games_info.keys():
        games_info[i]['source'] = get_source(games_info[i]['url'])
    a = get_pubg(games_info['pubg']['source'])
    b = get_r6(games_info['r6']['source'])
    c = get_lol(games_info['lol']['source'])
    renew = renew_token()
    access_token = renew['access_token']
    text = ''
    if a:
        text += 'pubg has released a new update \n'
    if b:
        text += 'r6 has released a new update \n'
    if c:
        text += 'lol has released a new update \n'
    if text != '':
        send_message(text)
    else:
        send_message('no new updates')

schedule.every().day.at("08:50").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)




