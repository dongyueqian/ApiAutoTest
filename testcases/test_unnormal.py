import pytest,requests
from public import common,files_utils
import json
from public.logger import logger

# test_data = [
#     ({"accesstoken":"","title": "新建主题--测试","tab": "ask","content": "测一下，打扰啦，抱歉抱歉～"}, 401, "错误的accessToken"),
#     ({"accesstoken":"1e0d9ca5-4ff3-4ce6-918d-8ba853ed6694","title": "","tab": "ask","content": "测一下，打扰啦，抱歉抱歉～"}, 400, "标题不能为空"),
#     ({"accesstoken":"1e0d9ca5-4ff3-4ce6-918d-8ba853ed6694","title": "新建主题--测试","tab": "","content": "测一下，打扰啦，抱歉抱歉～"}, 400, "必须选择一个版块"),
#     ({"accesstoken":"1e0d9ca5-4ff3-4ce6-918d-8ba853ed6694","title": "新建主题--测试","tab": "ask","content": ""},400, "内容不可为空"),
# ]

# json文件数据驱动
# test_data = json.load(open(r"data/topic_data.json",mode='r', encoding="utf8"))["test_data"]

test_data = files_utils.json_file(r"data/topic_data.json")

@pytest.mark.parametrize("topics_data,code,error_msg",test_data)
def test_create_topic(topics_data,code,error_msg):
    '''创建主题，参数不合法'''
    # print(test_data)
    r = common.create_topics(topics_data)
    logger.debug(f"发送请求: {r}")
    # print(r.json())
    assert r.status_code == code
    assert r.json()["error_msg"] == error_msg