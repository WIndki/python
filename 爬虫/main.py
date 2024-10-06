import requests
from bs4 import BeautifulSoup
import re
import json
import time

novel_pic_list = []
url = 'https://book.sfacg.com/List/default.aspx?tid=21&PageIndex='
error_page = []

for i in range(501, 3946):
    url_copy = url + str(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Referer': 'https://book.sfacg.com/'
    }
    response = requests.get(url_copy, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        uls = soup.find_all('ul', class_='Comic_Pic_List')
        if not uls:
            continue
        for ul in uls:
            links = ul.find_all('li')
            for link in links:
                strong_tag = link.find('strong')
                if not strong_tag:
                    continue
                book_name = strong_tag.text
                book_url = "https://book.sfacg.com" + strong_tag.a['href']
                author = link.find('a',id=re.compile('Author')).text
                info_text = link.text
                match1 = re.search(r'综合信息：.*', info_text, re.MULTILINE)
                if match1:
                    infomation = match1.group(0)
                    information = infomation.replace('综合信息：', '')
                    infomation = infomation.replace('\r', '')
                    pattern = re.compile(r'/ (\d+)字')
                    match2 = pattern.findall(infomation)
                    if match2:
                        word_count = int(match2[0])
                    novel_pic_list.append({
                        'book_name': book_name,
                        'book_url': book_url,
                        'author': author,
                        'infomation': infomation,
                        'word_count': word_count
                    })
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        error_page.append(i)
    time.sleep(0.2)

with open('./novel_pic_list.json', 'w', encoding='utf-8') as f:
        json.dump(novel_pic_list, f, ensure_ascii=False, indent=4)