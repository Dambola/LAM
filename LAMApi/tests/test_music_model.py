from lamapi.music.model import MusicManager
from lamapi.music.constants import OrderBy, FilterBy

from tests import client
from tests.config.music import *

import pytest

class TestMusicModel(object):
    @pytest.mark.run(order=1)
    def testAddOne(self, client):
        mgr = MusicManager()
        id, error = mgr.add(MUSIC_1)
        assert id and not error
    
    @pytest.mark.run(order=2)
    def testAddTwo(self, client):
        mgr = MusicManager()
        id, error = mgr.add(MUSIC_2)
        assert id and not error
    
    @pytest.mark.run(order=3)
    def testAddThree(self, client):
        mgr = MusicManager()
        id, error = mgr.add(MUSIC_3)
        assert id and not error

    @pytest.mark.run(order=4)
    def testEditOne(self, client):
        mgr = MusicManager()
        done, error = mgr.edit(MUSIC_1['id'], MUSIC_EDIT_1)
        assert done and not error
    
    @pytest.mark.run(order=5)
    def testSearchByNameOne(self, client):
        mgr = MusicManager()
        music = mgr.searchByName(MUSIC_EDIT_1['name'], MUSIC_EDIT_1['author'])
        assert music and self.__areTheSame(music, MUSIC_EDIT_1) 

    @pytest.mark.run(order=6)
    def testSearchByIDOne(self, client):
        mgr = MusicManager()
        music = mgr.searchByID(MUSIC_2['id'])
        assert music and self.__areTheSame(music, MUSIC_2) 

    @pytest.mark.run(order=7)
    def testEditTwo(self, client):
        mgr = MusicManager()
        done, error = mgr.edit(MUSIC_2['id'], MUSIC_EDIT_2)
        assert done and not error
    
    @pytest.mark.run(order=8)
    def testSearchAllOne(self, client):
        mgr = MusicManager()
        musics = mgr.searchAll(order_by=[OrderBy.Id.Asc])
        assert len(musics) == 3 and \
            self.__areTheSame(musics[0], MUSIC_EDIT_1) and \
            self.__areTheSame(musics[1], MUSIC_EDIT_2) and \
            self.__areTheSame(musics[2], MUSIC_3)
    
    @pytest.mark.run(order=9)
    def testSearchAllTwo(self, client):
        mgr = MusicManager()

        filters = [
            FilterBy.Name(MUSIC_EDIT_1['name'])
        ]

        musics = mgr.searchAll(filter_by=filters, order_by=[OrderBy.Id.Desc])
        assert len(musics) == 1 and \
            self.__areTheSame(musics[0], MUSIC_EDIT_1)

    @pytest.mark.run(order=10)
    def testSearchAllThree(self, client):
        mgr = MusicManager()

        filters = [
            FilterBy.Author(
                MUSIC_EDIT_1['author'],
                MUSIC_EDIT_2['author']
            ),
        ]

        musics = mgr.searchAll(filter_by=filters,order_by=[OrderBy.Id.Desc])
        assert len(musics) == 2 and \
            self.__areTheSame(musics[0], MUSIC_EDIT_2) and \
            self.__areTheSame(musics[1], MUSIC_EDIT_1)

    @pytest.mark.run(order=11)
    def testSearchAllFour(self, client):
        mgr = MusicManager()
        musics = mgr.searchAll(order_by=[OrderBy.Id.Asc])
        assert len(musics) == 3 and \
            self.__areTheSame(musics[0], MUSIC_EDIT_1) and \
            self.__areTheSame(musics[1], MUSIC_EDIT_2) and \
            self.__areTheSame(musics[2], MUSIC_3)
    
    @pytest.mark.run(order=12)
    def testRemoveOne(self, client):
        mgr = MusicManager()
        removed, error = mgr.remove(MUSIC_1['id'])
        assert removed and not error

    @pytest.mark.run(order=13)
    def testRemoveTwo(self, client):
        mgr = MusicManager()
        removed, error = mgr.remove(MUSIC_2['id'])
        assert removed and not error

    @pytest.mark.run(order=14)
    def testRemoveThree(self, client):
        mgr = MusicManager()
        removed, error = mgr.remove(MUSIC_3['id'])
        assert removed and not error
    
    @pytest.mark.run(order=15)
    def testRemoveFails(self, client):
        fake_music_id = 4
        mgr = MusicManager()
        removed, error = mgr.remove(fake_music_id)
        assert not removed and error

    def __areTheSame(self, one, two):
        return one['id'] == two['id'] and \
            one['name'] == two['name'] and \
            one['author'] == two['author'] and \
            one['type1'] == two['type1'] and \
            one['type2'] == two['type2'] and \
            one['type3'] == two['type3']
    