import requests
import urllib.parse
import json
import re
import threading
from time import sleep
from bs4 import BeautifulSoup
from tqdm import tqdm
import os

__USER_AGENT__ = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
__REFERER__ = 'https://movie.douban.com/explore'
__ORIGIN__ = 'https://movie.douban.com'

#Headers预设值
__HEADER__ = {
    'User-Agent': __USER_AGENT__,
    'Referer': __REFERER__,
    'Origin': __ORIGIN__,
}

def get_movie_info(movieId, url):
    #预设list
    movieInfo = {}
    try:
        response = requests.get(url, headers=__HEADER__)    #发起请求
        if response.status_code == 200:    #检查请求状态
            soup = BeautifulSoup(response.text, 'html.parser')  #解析为HTML格式
            movieName = soup.find('span', property='v:itemreviewed').text         #获取电影名称
            info = soup.find('div', id='info')      #获取电影信息面板
            try:
                movieDirector = info.find('a', rel='v:directedBy').text    #获取导演
            except:
                movieDirector = '无'

            try:
                movieActors = [actor.text for actor in info.find_all('a', rel='v:starring')]    #获取演员
            except:
                movieActors = '无'

            try:
                movieType = [mtype.text for mtype in info.find_all('span', property='v:genre')]    #获取类型
            except:
                movieType = '无'

            try:
                movieDate = info.find('span', property='v:initialReleaseDate').text    #获取上映日期
            except:
                movieDate = '无'

            try:
                movieRuntime = info.find('span', property='v:runtime').text    #获取片长
            except:
                movieRuntime = '无'

            try:
                movieRating = soup.find('div', rel='v:rating')   #获取评分面板
                score = movieRating.find('strong', property='v:average').text    #获取平均分
                scoreItem = movieRating.find_all('div', class_='item') #获取评分百分比
                scorePercent = {}
                for item in scoreItem:
                    star_text = item.find('span', class_='starstop').text
                    star_match = re.search(r'(\d)星', star_text)
                    if star_match:
                        star = star_match.group(1)
                        scorePercent[star] = item.find('span', class_='rating_per').text #获取评分百分比
            except:
                score = '无'
                scorePercent = {}
            movieInfo = {
                'name': movieName,
                'id': movieId,
                'director': movieDirector,
                'actors': movieActors,
                'type': movieType,
                'date': movieDate,
                'runtime': movieRuntime,
                'score': score,
                'scorePercent': scorePercent,
            }
            response.close()
        else:
            response.close()
    except requests.RequestException as e:
            print(f"Request failed: {e}")
            return {}
    return movieInfo

def fetch_movie_info(movie, movies):
    movieId = movie.get('id')
    url = f'https://movie.douban.com/subject/{movieId}/'
    movieInfo = get_movie_info(movieId, url)
    if movieInfo:
        movies.append(movieInfo)

#URL预设值
movies = []
with open('test.json', 'r', encoding='utf-8') as f:
    datas = json.load(f)
threads = []
max_threads = 5
active_threads = 0
progress_bar = tqdm(total=len(datas), desc="Fetching movie info", unit="movie")
for movie in datas:
    thread = threading.Thread(target=fetch_movie_info, args=(movie, movies))
    if active_threads >= max_threads:
        for t in threads:
            t.join()
            active_threads -= 1
    threads.append(thread)
    progress_bar.update(1)
    thread.start()
    active_threads += 1

progress_bar.close()

for thread in threads:
    thread.join()

if not os.path.exists('movies_info.json'):
    with open('movies_info.json', 'w', encoding='utf-8') as f:
        json.dump([], f, ensure_ascii=False, indent=4)

with open('movies_info.json', 'r', encoding='utf-8') as f:
    movie_old = json.load(f)
    f.seek(0)  # Move the cursor to the beginning of the file
    for movie in movies:
        movie_old.append(movie)

with open('movies_info.json', 'w', encoding='utf-8') as f:
    json.dump(movie_old, f, ensure_ascii=False, indent=4)

