from lamapi.music.model import MusicManager
from lamapi.music.constants import OrderBy, FilterBy

from tests.config import User1 
from tests.config.music import *
from tests.utils import doLogin
from tests import client

import pytest

class TestMusicController(object):
    pass
#     url = '/music'


#     # ---- Create Scope Methods

#     def __create_music(self, client, user, music):
#         rv = doLogin(client, user.login, user.password)
        
#         data = dict(
#             name = music.name,
#             author = music.author,
#             type1 = music.type1,
#             type2 = music.type2,
#             type3 = music.type3,
#         )

#         return client.put(self.url, data=data, follow_redirects=True)

#     @pytest.mark.run(order=6)
#     def testMusicCreation1(self, client):
#         response = self.__create_music(client, User1, Music1)
#         data = response.get_json()
#         if response.status_code == 400:
#             raise Exception(data['message'])
#         assert response.status_code == 200

#     @pytest.mark.run(order=7)
#     def testMusicCreation2(self, client):
#         response = self.__create_music(client, User1, Music2)
#         data = response.get_json()
#         if response.status_code == 400:
#             raise Exception(data['message'])
#         assert response.status_code == 200
    

#     # ---- Delete Scope Methods

#     def __delete_music(self, music):
#         self.__search_music(music).doDelete()
    
#     @pytest.mark.run(order=8)
#     def testMusicDelete1(self):
#         self.__delete_music(Music1)
#         music = self.__search_music(Music1)
#         assert music is None
    
#     @pytest.mark.run(order=9)
#     def testMusicDelete2(self):
#         self.__delete_music(Music2)
#         music = self.__search_music(Music2)
#         assert music is None
    
    
#     # ---- Search Scope Methods

#     def __search_music(self, music):
#         return Music.query \
#             .filter_by(name=music.name, author=music.author) \
#                 .first()
