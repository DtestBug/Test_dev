import random
import time


def sleep(n_secs):
    time.sleep(n_secs)


def get_random_user_agent():
    users_agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36']
    return random.choice(users_agent)


def get_accounts():
    # 如果要实现参数化（数据驱动），那么要返回一个嵌套字典的列表
    # 1.每个字典代表一条用例
    # 2.每个字典的key为变量名
    accounts = [
        {"title": "正常登录", "username": "jiuge1", "password": "123456", "status_code": 200, "contain_msg": "token"},
        {"title": "密码错误", "username": "test", "password": "111111", "status_code": 400, "contain_msg": "errors"},
        {"title": "账号错误", "username": "tttt", "password": "123456", "status_code": 400, "contain_msg": "errors"},
        {"title": "用户为空", "username": "", "password": "123456", "status_code": 400, "contain_msg": "username"},
        {"title": "密码为空", "username": "test", "password": "", "status_code": 400, "contain_msg": "password"},
    ]
    return accounts


if __name__ == '__main__':
    get_random_user_agent()
