import unittest

from user import User
from user.user_repository import UserRepository


class UserTest(unittest.TestCase):
    def test_user(self):
        user_repo = UserRepository()

        user1 = User(name="John", password="pass123")
        user2 = User(name="Admin", password="adminpass", is_admin=True)

        user_repo.add_user(user1)
        user_repo.add_user(user2)

        assert user_repo.find_by_name("John")
        assert user_repo.find_by_name("Admin")

        assert not user1.is_authenticated
        assert not user1.authenticate("John", "wrongpass")
        user1.authenticate("John", "pass123")
        assert user1.is_authenticated

        user2.authenticate("Admin", "adminpass")

        user_repo.logout_all_except_admins()
        
        assert not user1.is_authenticated
        assert user2.is_authenticated
