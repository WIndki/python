import json
import re
# 定义 JSON 文件的路径
json_file_path = './novel_pic_list.json'

# 读取 JSON 文件
with open(json_file_path, 'r', encoding='utf-8') as file:
    novel_pic_list = json.load(file)

novel_pic_list_new = []
for novel in novel_pic_list:
    # 从综合信息中提取出字数和状态
    if novel['word_count'] > 500000:
        word_count = round(float(novel['word_count']) / 10000, 2)
        novel['infomation'] = novel['infomation'].replace(f'{novel['word_count']}', f'{word_count}万')
        novel_pic_list_new.append(novel)

with open('./novel_pic_list_new.json', 'w', encoding='utf-8') as f:
    json.dump(novel_pic_list_new, f, ensure_ascii=False, indent=4)