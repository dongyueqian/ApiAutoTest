import datetime
import pytest
import requests
from public import common
from public.logger import logger

base_url = "http://47.100.175.62:3000/api/v1"

def test_topics_index_page():
    '''get /topics 主题首页'''
    params = {
        'page': 1,
        'tab': 'ask',
        'limit': 2,
        'mdrender': 'false',
    }
    r = requests.get(base_url+"/topics", params=params)
    logger.debug(f"发送请求: {r}")
    assert r.status_code == 200
    assert r.json()['success'] == True
    data = r.json()['data']
    for i in data:
        assert i['tab'] == params['tab']
        print('----断言----')

@pytest.mark.skip(reason="跳过创建主题用例")
def test_create_topic():
    '''post /topics 新建主题'''
    topics_data = {
        "accesstoken":common.get_accesstoken(),
        "title":"新建主题--测试",
        "tab":"ask",
        "content":"测一下，打扰啦，抱歉抱歉～",
    }
    r = common.create_topics(topics_data)
    logger.debug(f"发送请求: {r}")
    print(r.json())
    assert r.status_code == 200
    assert r.json()["success"] == True

    r2 = common.create_topics(topics_data)
    assert r2.json()["topic_id"] != r.json()["topic_id"]

def test_update_topic():
    '''post /topics/update 编辑主题'''
    topics_data = {
        "accesstoken": common.get_accesstoken(),
        "title": "新建主题--测试"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "tab": "ask",
        "content": "测一下，打扰啦，抱歉抱歉～",
    }
    r = common.create_topics(topics_data)
    logger.debug(f"发送请求: {r}")
    id = r.json()["topic_id"]
    # id = "6162b2269017021fcfdbc78e"

    updata_topic_data = {
        "accesstoken": common.get_accesstoken(),
        "topic_id":id,
        "title": "更新主题--测试"+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "tab": "ask",
        "content": "测一下更新，打扰啦，抱歉抱歉～",
    }
    r2 = requests.post(base_url+"/topics/update", json=updata_topic_data)
    logger.debug(f"发送请求: {r2}")
    print(r2.json())

    assert r2.json()["topic_id"] == id

    r_detail = common.topic_detail(id).json()
    print(r_detail)
    assert r_detail["data"]["id"] == id
    assert r_detail["data"]["tab"] == updata_topic_data["tab"]
    assert r_detail["data"]["title"] == updata_topic_data["title"]
    assert updata_topic_data["content"] in r_detail["data"]["content"]


if __name__ == '__main__':
    pytest.main(['-v'])