import requests
import bs4
import schedule
import time

games_info = {
    'pubg': {'url': 'https://www.pubg.com/category/patch-notes-en-gb/', 'source': ''},
    'r6' : {'url':'https://www.ubisoft.com/en-us/game/rainbow-six/siege/news-updates', 'source':''},
    'lol' : {'url':'https://na.leagueoflegends.com/en-us/news/game-updates/', 'source':''}
}

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
        print('no change for pubg')
    else:
        date_check('pubg.txt', 'w', new_date)
        print('success')

def get_lol(source):
    new_date = source.find('h2',class_='style__Title-i44rc3-8 jprNto').text
    old_date = date_check('lol.txt', 'r')
    if old_date == new_date:
        print('no change for lol')
    else:
        date_check('lol.txt', 'w', new_date)
        print('success')

def get_r6(source):
    new_date = source.find('span',class_='date__day').text
    old_date = date_check('r6.txt', 'r')
    if old_date == new_date:
        print('no change for r6')
    else:
        date_check('r6.txt', 'w', new_date)
        print('success')

def job():
    for i in games_info.keys():
        games_info[i]['source'] = get_source(games_info[i]['url'])
    get_pubg(games_info['pubg']['source'])
    get_r6(games_info['r6']['source'])
    get_lol(games_info['lol']['source'])

schedule.every().day.at("08:50").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)