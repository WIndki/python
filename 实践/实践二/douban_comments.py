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
movieId = '36246315'
url = f'https://movie.douban.com/subject/{movieId}/comments?start=0&limit=20&status=P&sort=new_score'

#预设list
movieCommentInfos = []
try:
    response = requests.get(url, headers=__HEADER__)    #发起请求
    if response.status_code == 200:    #检查请求状态
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        commentItems = soup.find_all('div', class_='comment-item')
        for item in commentItems:
            commentInfo = item.find('span', class_='comment-info')
            user = commentInfo.find('a', class_='')
            comment = item.find('span', class_='short').text
            movieCommentInfos.append({
                'user': user.text,
                'userurl': user['href'],
                'comment': comment,
            })

except requests.RequestException as e:
        print(f"Request failed: {e}")
finally:
    #关闭请求
    response.close()

#输出结果
print(json.dumps(movieCommentInfos, ensure_ascii=False, indent=4))
