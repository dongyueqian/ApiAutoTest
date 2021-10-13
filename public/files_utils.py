import json
import allure

# 封装文件处理方法
# @allure.story("处理json文件")
def json_file(file_path):
    json_data = json.load(open(file_path, mode='r', encoding="utf8"))["test_data"]
    return json_data