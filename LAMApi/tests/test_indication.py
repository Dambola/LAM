from lamapi.auth.model import User
from lamapi.indication.model import IndicationManager
from lamapi.music.model import Music

from tests.config import Indication1, Indication2, Indication3 
from tests.utils import doLogin
from tests import client
import pytest

class TestIndicationManager(object):


    # ---- Add tests

    @pytest.mark.run(order=10)
    def testAddIndication1(self):
        indication_id = self.__add_indication(Indication1)
        Indication1.id = indication_id
        assert indication_id

    @pytest.mark.run(order=11)
    def testAddIndication2(self):
        indication_id = self.__add_indication(Indication2)
        Indication2.id = indication_id
        assert indication_id 

    @pytest.mark.run(order=12)
    def testAddIndication3(self, client):
        indication_id = self.__add_indication(Indication3)
        assert not indication_id


    # ---- Search tests

    @pytest.mark.run(order=13)
    def testGetAllIndications(self):
        manager = IndicationManager()
        indications = manager.getAllIndications()
        
        assert self.__is_inside(Indication1.id, indications) and \
            self.__is_inside(Indication2.id, indications)
    
    @pytest.mark.run(order=14)
    def testGetAllIndicationsWithCriteria(self):
        manager = IndicationManager()
        criteria1 = dict(name=Indication1.name, author=Indication1.author)
        criteria2 = dict(name=Indication2.name, author=Indication2.author)
        indications = manager.getAllIndications(criteria1, criteria2)

        assert self.__is_inside(Indication1.id, indications) and \
            self.__is_inside(Indication2.id, indications)
    
    @pytest.mark.run(order=15)
    def testGetAnIndication(self):
        manager = IndicationManager()

        by_id = Indication1.id
        by_dict = self.__indication_to_dict(Indication2)

        indication_1 = manager.getAnIndication(by_id)
        indication_2 = manager.getAnIndication(by_dict)

        assert indication_1 and indication_2


    # ---- Refuse tests

    @pytest.mark.run(order=16)
    def testRefuseIndication(self):
        manager = IndicationManager()

        by_id = Indication1.id

        manager.refuseIndication(by_id)
        indication = manager.getAnIndication(by_id)
        music = Music.query \
            .filter_by(name=Indication1.name, author=Indication1.author) \
                .first()

        assert (not indication) and (not music)
    

    # ---- Approve tests

    @pytest.mark.run(order=17)
    def testApproveIndication(self):
        manager = IndicationManager()

        by_id = Indication2.id
        
        manager.approveIndication(by_id)
        indication = manager.getAnIndication(by_id)
        music = Music.query \
            .filter_by(name=Indication2.name, author=Indication2.author) \
                .first()
        
        is_music = music is not None
        music.doDelete()

        assert (not indication) and is_music
    

    # ---- Internal methods

    def __is_inside(self, _id, _indications):
        for indication in _indications:
            if indication.id == _id:
                return True
        return False

    def __add_indication(self, indication):
        try:
            manager = IndicationManager()
            data = self.__indication_to_dict(indication)
            return manager.addIndication(data)
        except Exception as e:
            raise e

    def __indication_to_dict(self, indication):
        return {
            'name' : indication.name,
            'author': indication.author,
            'type1' : indication.type1,
            'type2' : indication.type2,
            'type3' : indication.type3,
            'user'  : User.getUserId(indication.user.login),
            'link'  : indication.link,
        }
