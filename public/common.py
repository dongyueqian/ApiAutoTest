import requests

# 公用方法

def get_accesstoken():
    return "1e0d9ca5-4ff3-4ce6-918d-8ba853ed6694"

def create_topics(topics_data):
    url = "http://47.100.175.62:3000/api/v1/topics"
    r = requests.post(url=url, json=topics_data)
    return r

def topic_detail(id):
    '''get /topic/:id 主题详情'''
    url = "http://47.100.175.62:3000/api/v1/topic/"+id
    return requests.get(url)
