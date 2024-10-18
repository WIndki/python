import requests
import urllib.parse
import json
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

def get_movie_index(tag, category, sort, count, url):
    #预设list
    movies = []
    #发起请求
    try:
        response = requests.get(url, headers=__HEADER__)
        #检查请求状态
        if response.status_code == 200:
            #解析为JSON格式
            data = response.json()
            # 解析并打印电影标题
            for movie in data.get('items', []):
                title = movie.get('title')
                if title:
                    movies.append(movie)
    except requests.RequestException as e:
            print(f"Request failed: {e}")
    finally:
        #关闭请求
        response.close()
    return movies

def save_movie_info(movies, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(movies, ensure_ascii=False, indent=4))

tag = '华语'
category = f'{{"地区":"{tag}"}}'
sort = 'S'
count = '200'
url = f'https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count={count}&selected_categories={category}&uncollect=false&sort={sort}&tags={tag}'
movies = get_movie_index(tag, category, sort, count, url)
save_movie_info(movies, f'{tag}.json')
