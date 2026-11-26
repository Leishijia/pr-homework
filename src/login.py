"""极简登录校验模块。

示例项目：为了练习 Pull Request 流程，初始版本故意保留了几个缺陷，
本次提交针对 README.md 中「已知问题」做修复。
"""

USERS = {
    "alice": "alice@123",
    "bob": "bob@456",
}


def verify_login(username, password):
    """校验用户名与密码是否匹配。

    匹配返回 True，否则返回 False。

    修复要点：
    - 用户名/密码为空或非字符串时直接拒绝，不再抛 KeyError；
    - 用户名做 strip + lower 规范化，忽略首尾空格与大小写；
    - 未知用户返回 False 而不是抛异常。
    """
    if not isinstance(username, str) or not isinstance(password, str):
        return False

    username = username.strip().lower()
    if not username or not password:
        return False

    return USERS.get(username) == password
