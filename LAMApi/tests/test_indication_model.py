from lamapi.indication.model import IndicationManager
from lamapi.indication.constants import OrderBy, FilterBy

from tests import client
from tests.config.indication import *

import pytest

class TestIndicationModel(object):
    @pytest.mark.run(order=16)
    def testAddOne(self, client):
        mgr = IndicationManager()
        id, error = mgr.add(INDICATION_1)
        assert id and not error
    
    @pytest.mark.run(order=17)
    def testAddTwo(self, client):
        mgr = IndicationManager()
        id, error = mgr.add(INDICATION_2)
        assert id and not error
    
    @pytest.mark.run(order=18)
    def testAddThree(self, client):
        mgr = IndicationManager()
        id, error = mgr.add(INDICATION_3)
        assert id and not error

    @pytest.mark.run(order=19)
    def testSearchByNameOne(self, client):
        mgr = IndicationManager()
        indication = mgr.searchByName(INDICATION_1['name'], 
            INDICATION_1['author'])
        assert indication and self.__areTheSame(indication, INDICATION_1) 

    @pytest.mark.run(order=20)
    def testSearchByIDOne(self, client):
        mgr = IndicationManager()
        indication = mgr.searchByID(INDICATION_2['id'])
        assert indication and self.__areTheSame(indication, INDICATION_2) 

    @pytest.mark.run(order=21)
    def testEdit(self, client):
        mgr = IndicationManager()
        done, error = mgr.edit(INDICATION_EDIT_3['id'], 
            INDICATION_EDIT_3)
        assert done and not error

    @pytest.mark.run(order=22)
    def testSearchAllOne(self, client):
        mgr = IndicationManager()
        indications = mgr.searchAll(order_by=[OrderBy.Id.Asc])
        assert len(indications) == 3 and \
            self.__areTheSame(indications[0], INDICATION_1) and \
            self.__areTheSame(indications[1], INDICATION_2) and \
            self.__areTheSame(indications[2], INDICATION_EDIT_3)
    
    @pytest.mark.run(order=23)
    def testSearchAllTwo(self, client):
        mgr = IndicationManager()

        filters = [
            FilterBy.Name(
                INDICATION_1['name'], 
                INDICATION_2['name']
            )
        ]

        indications = mgr.searchAll(filter_by=filters, order_by=[OrderBy.Id.Desc])
        assert len(indications) == 2 and \
            self.__areTheSame(indications[0], INDICATION_2) and \
            self.__areTheSame(indications[1], INDICATION_1)

    @pytest.mark.run(order=24)
    def testSearchAllThree(self, client):
        mgr = IndicationManager()

        filters = [
            FilterBy.Author(
                INDICATION_1['author']
            )
        ]

        indications = mgr.searchAll(filter_by=filters,order_by=[OrderBy.Id.Asc])
        assert len(indications) == 2 and \
            self.__areTheSame(indications[0], INDICATION_1) and \
            self.__areTheSame(indications[1], INDICATION_2)

    @pytest.mark.run(order=25)
    def testSearchAllFour(self, client):
        mgr = IndicationManager()
        indications = mgr.searchAll(order_by=[OrderBy.Id.Desc])
        assert len(indications) == 3 and \
            self.__areTheSame(indications[0], INDICATION_EDIT_3) and \
            self.__areTheSame(indications[1], INDICATION_2) and \
            self.__areTheSame(indications[2], INDICATION_1)
    
    @pytest.mark.run(order=26)
    def testApprove(self, client):
        mgr = IndicationManager()
        music_id, error = mgr.approve(INDICATION_1['id'])
        indication = mgr.searchByID(INDICATION_1['id'])
        assert music_id and not error and not indication
    
    @pytest.mark.run(order=27)
    def testApprove(self, client):
        mgr = IndicationManager()
        music_id, error = mgr.approve(INDICATION_2['id'])
        indication = mgr.searchByID(INDICATION_2['id'])
        assert music_id and not error and not indication
    
    @pytest.mark.run(order=28)
    def testDelete(self, client):
        mgr = IndicationManager()
        done, error = mgr.delete(INDICATION_EDIT_3['id'])
        indication = mgr.searchByID(INDICATION_EDIT_3['id'])
        assert done and not error and not indication

    def __areTheSame(self, one, two):
        return one['id'] == two['id'] and \
            one['name'] == two['name'] and \
            one['author'] == two['author'] and \
            one['type1'] == two['type1'] and \
            one['type2'] == two['type2'] and \
            one['type3'] == two['type3'] and \
            one['link'] == two['link'] and \
            one['user'] == two['user']
    
