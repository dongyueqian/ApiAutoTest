import requests
import allure

# 公用方法

# @allure.story("获取token")
def get_accesstoken():
    return "1e0d9ca5-4ff3-4ce6-918d-8ba853ed6694"

# @allure.story("创建话题")
def create_topics(topics_data):
    url = "http://47.100.175.62:3000/api/v1/topics"
    r = requests.post(url=url, json=topics_data)
    return r

# @allure.story("查看话题详情")
def topic_detail(id):
    '''get /topic/:id 主题详情'''
    url = "http://47.100.175.62:3000/api/v1/topic/"+id
    return requests.get(url)
