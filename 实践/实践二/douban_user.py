import requests
import urllib.parse
import json
import re
from bs4 import BeautifulSoup
__USER_AGENT__ = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
__REFERER__ = 'https://movie.douban.com/explore'
__ORIGIN__ = 'https://movie.douban.com'
#Headers预设值
__HEADER__ = {
    'User-Agent': __USER_AGENT__,
    'Referer': __REFERER__,
    'Origin': __ORIGIN__,
}

#URL预设值
user_id = 'https://www.douban.com/people/aloysius14/'
url = f'{user_id}collect?start=1'
url = url.replace('https://www.douban.com/people/', 'https://movie.douban.com/people/')
#预设list
visitedMovie = []
try:
    response = requests.get(url, headers=__HEADER__)    #发起请求
    if response.status_code == 200:    #检查请求状态
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        movieItems = soup.find_all('div', class_='item comment-item')
        for item in movieItems:
            movieInfo = item.find('div', class_='info')
            movie = movieInfo.find('li', class_='title').find('a')
            score = movieInfo.find('span', class_=re.compile(r'rating\d-t'))
            visitedMovie.append({
                'movie': movie.text.replace('\n', '').replace(' ', ''),
                'url': movie['href'],
                'score': score.text if score else '未评分',
            })
except requests.RequestException as e:
        print(f"Request failed: {e}")
finally:
    #关闭请求
    response.close()

#输出结果
print(json.dumps(visitedMovie, ensure_ascii=False, indent=4))
