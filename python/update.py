import requests
import bs4

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

for i in games_info.keys():
    games_info[i]['source'] = get_source(games_info[i]['url'])
print(games_info)