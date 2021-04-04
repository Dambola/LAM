from lamapi.auth.model import User

from tests.config import User1

import pytest

class TestUser(object):
    pass
    # @pytest.mark.run(order=1)
    # def testUserCreation(self):
    #     user = User1
    #     user_created = False

    #     if not User.getUserId(user.login):
    #         User(login=user.login, password=user.password, email=user.email).doSave()
    #         user_created = True
        
    #     assert user_created
    
    # @pytest.mark.run(order=20)
    # def testUserDelete(self):
    #     user = User1

    #     user_id = User.getUserId(user.login)
    #     User.query.filter_by(id=user_id).first().doDelete()
        
    #     assert User.getUserId(user.login) is None