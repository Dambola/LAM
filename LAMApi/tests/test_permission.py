from lamapi.auth.model import User
from lamapi.config import PermissionConfig
from lamapi.permission.model import Permission

import string
import pytest
import random

LOGIN = None 
PASSWORD = None
EMAIL = None

def generateRandomUser(size):
    global LOGIN, PASSWORD, EMAIL

    alphabet = string.ascii_lowercase

    login = ''.join([alphabet[random.randint(0, len(alphabet) - 1)] \
        for i in range(size)])
    password = ''.join([alphabet[random.randint(0, len(alphabet) - 1)] \
        for i in range(size)])
    email = login + '@testing.com.br'
    
    LOGIN = login
    PASSWORD = password
    EMAIL = email

class TestPermission(object):
    PERMISSION_1 = PermissionConfig.ADD_MUSIC
    PERMISSION_2 = PermissionConfig.DEL_MUSIC
    PERMISSION_3 = PermissionConfig.EDT_MUSIC

    @pytest.mark.dependency()
    def testUserCreation(self):
        tries = 0
        max_tries = 30
        user_created = False

        while not user_created:
            generateRandomUser(30)

            if not User.getUserId(LOGIN):
                new_user = User(login=LOGIN, password=PASSWORD, email=EMAIL)
                new_user.saveToDb()
                user_created = True
            
            tries += 1
        
        assert new_user and user_created and tries <= max_tries

    @pytest.mark.dependency(depends=["TestPermission::testUserCreation"])
    def testPermissionInsert(self):
        user_id = User.getUserId(LOGIN)

        perm_1 = Permission(permission=self.PERMISSION_1, user=user_id)
        perm_1.saveToDb()

        perm_2 = Permission(permission=self.PERMISSION_2, user=user_id)
        perm_2.saveToDb()

        perm_3 = Permission(permission=self.PERMISSION_3, user=user_id)
        perm_3.saveToDb()

        all_perms = Permission.getPermissions(LOGIN)
        assert self.PERMISSION_1 in all_perms and \
            self.PERMISSION_2 in all_perms and \
                self.PERMISSION_3 in all_perms
    
    @pytest.mark.dependency(depends=["TestPermission::testPermissionInsert"])
    def testPermissionSelect(self):
        assert Permission.hasPermission(LOGIN, self.PERMISSION_1) and \
            Permission.hasPermission(LOGIN, self.PERMISSION_2) and \
                Permission.hasPermission(LOGIN, self.PERMISSION_3)

    @pytest.mark.dependency(depends=["TestPermission::testPermissionSelect"])
    def testPermissionDelete(self):
        user_id = User.getUserId(LOGIN)
        
        perms = Permission.query.filter_by(user=user_id)
        perms.delete()

        assert not Permission.hasPermission(LOGIN, self.PERMISSION_1) and \
            not Permission.hasPermission(LOGIN, self.PERMISSION_2) and \
                not Permission.hasPermission(LOGIN, self.PERMISSION_3)

    @pytest.mark.dependency(depends=["TestPermission::testPermissionDelete"])
    def testUserDelete(self):
        user_id = User.getUserId(LOGIN)
        User.query.filter_by(id=user_id).delete()
        
        assert User.getUserId(LOGIN) is None
    

