"""verify_login 的单元测试。"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.login import verify_login


class TestVerifyLogin(unittest.TestCase):
    def test_correct_credentials_pass(self):
        """正确的用户名和密码应当登录成功。"""
        self.assertTrue(verify_login("alice", "alice@123"))

    def test_wrong_password_rejected(self):
        """密码错误应当被拒绝。"""
        self.assertFalse(verify_login("alice", "wrong-password"))

    def test_unknown_user_rejected(self):
        """不存在的用户应当返回 False，而不是抛异常。"""
        self.assertFalse(verify_login("nobody", "whatever"))

    def test_empty_input_rejected(self):
        """空用户名/空密码应当返回 False，而不是抛异常。"""
        self.assertFalse(verify_login(None, None))

    def test_username_case_insensitive(self):
        """用户名应当忽略大小写与首尾空格。"""
        self.assertTrue(verify_login("Alice", "alice@123"))
        self.assertTrue(verify_login("  alice  ", "alice@123"))


if __name__ == "__main__":
    unittest.main()
