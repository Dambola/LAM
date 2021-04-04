from lamapi.auth.model import User
from lamapi.config import PermissionConfig
from lamapi.permission.model import Permission

from tests.config import User1

import string
import pytest
import random

class TestPermission(object):
    pass
    # @pytest.mark.run(order=2)
    # def testPermissionInsert1(self):
    #     user = User1
    #     perm = PermissionConfig.ADD_MUSIC
    #     user_id = User.getUserId(user.login)

    #     permission = Permission(permission=perm, user=user_id)
    #     permission.doSave()

    #     all_perms = Permission.getPermissions(user.login)
    #     assert perm in all_perms

    # @pytest.mark.run(order=3)
    # def testPermissionInsert2(self):
    #     user = User1
    #     perm = PermissionConfig.DEL_MUSIC
    #     user_id = User.getUserId(user.login)

    #     permission = Permission(permission=perm, user=user_id)
    #     permission.doSave()

    #     all_perms = Permission.getPermissions(user.login)
    #     assert perm in all_perms

    # @pytest.mark.run(order=4)
    # def testPermissionInsert3(self):
    #     user = User1

    #     perm = PermissionConfig.EDT_MUSIC
    #     user_id = User.getUserId(user.login)

    #     permission = Permission(permission=perm, user=user_id)
    #     permission.doSave()

    #     all_perms = Permission.getPermissions(user.login)
    #     assert perm in all_perms
    
    # @pytest.mark.run(order=5)
    # def testHasPermission(self):
    #     user = User1

    #     perm_1 = PermissionConfig.ADD_MUSIC
    #     perm_2 = PermissionConfig.DEL_MUSIC
    #     perm_3 = PermissionConfig.EDT_MUSIC

    #     assert Permission.hasPermission(user.login, perm_1) and \
    #         Permission.hasPermission(user.login, perm_2) and \
    #             Permission.hasPermission(user.login, perm_3)

    # @pytest.mark.run(order=18)
    # def testPermissionDeleteAll(self):
    #     user = User1
    #     user_id = User.getUserId(user.login)

    #     perm_1 = PermissionConfig.ADD_MUSIC
    #     perm_2 = PermissionConfig.DEL_MUSIC
    #     perm_3 = PermissionConfig.EDT_MUSIC
        
    #     Permission.deletePermission(None, perm_1, user_id=user_id)
    #     Permission.deletePermission(None, perm_2, user_id=user_id)
    #     Permission.deletePermission(None, perm_3, user_id=user_id)

    #     assert not Permission.hasPermission(user.login, perm_1) and \
    #         not Permission.hasPermission(user.login, perm_2) and \
    #             not Permission.hasPermission(user.login, perm_3)

    
    

