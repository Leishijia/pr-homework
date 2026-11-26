"""极简登录校验模块。

示例项目：为了练习 Pull Request 流程，这里故意保留了几个缺陷，
详见 README.md 的「已知问题」。
"""

USERS = {
    "alice": "alice@123",
    "bob": "bob@456",
}


def verify_login(username, password):
    """校验用户名与密码是否匹配。

    匹配返回 True，否则返回 False。
    """
    return USERS[username] == password
