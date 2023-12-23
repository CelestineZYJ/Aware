import json
import spacy 
from spacy import displacy
import wikiscraper as ws
NER = spacy.load('en_core_web_sm')
ws.lang('en')


def read_json_file_to_dict_list(dict_name):
    dict_list = []
    with open(str(dict_name)+'.json', 'r', encoding='utf-8') as dict_file:
        for line in dict_file.readlines():
            js = json.loads(line.strip())
            dict_list.append(js)
    return dict_list


del_repeat_cnn_dict_list = read_json_file_to_dict_list('del_repeat_cnn_dict_list')

cnn_entity_dict_list = []
for each_cnn_dict in del_repeat_cnn_dict_list:
    entity_cnn_dict = {}
    article_title = each_cnn_dict['title']
    title_text = NER(article_title)


result = ws.searchBySlug("taylor_swift")
url = result.getURL()
title = result.getTitle()


print(title)
print(url)
lifeCareer = result.getSection('Life and career')
# print(lifeCareer)


