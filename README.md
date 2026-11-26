# pr-homework

一个小型示例项目，用于练习开源协作的完整流程：Fork → Clone → Branch → Commit → Push → Pull Request。

## 项目结构

```
pr-homework/
├── README.md
├── src/
│   ├── __init__.py
│   └── login.py          # 登录校验逻辑
└── tests/
    └── test_login.py     # 单元测试
```

## 功能说明

`src/login.py` 提供 `verify_login(username, password)`，校验用户名与密码是否匹配，
匹配返回 `True`，否则返回 `False`。

## 已修复问题（见 PR #2）

1. ~~**未做空值校验**：传入 `None` 或空字符串时抛出 `KeyError`。~~ 已改为返回 `False`。
2. ~~**用户名大小写敏感**：`Alice` 无法登录。~~ 已对用户名做 `strip().lower()` 规范化。
3. ~~**未知用户抛出异常**：直接 `KeyError`。~~ 已改为返回 `False`。

## 运行测试

```bash
python -m unittest discover -s tests -v
```

初始状态下上述 3 个用例为失败状态（FAILED），修复后应全部通过（OK）。

## 参与贡献

1. Fork 仓库到你自己的账号
2. `git clone https://github.com/<你的用户名>/pr-homework.git`
3. `git checkout -b fix-login-bug`
4. 修改代码并提交，推送到你自己的仓库
5. 向本仓库发起 Pull Request
