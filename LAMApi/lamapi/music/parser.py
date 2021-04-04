from lamapi.utils.api import Parser, ParserMeta
from flask_restful.reqparse import RequestParser

class MusicGetParser(Parser, metaclass=ParserMeta):
    def doSetup(self):
        pass
        

class MusicPutParser(Parser, metaclass=ParserMeta):
    def doSetup(self):
        self._parser.add_argument('name', location='json', help = 'Este campo é obrigatório', required = True)
        self._parser.add_argument('author', location='json', help = 'Este campo é obrigatório', required = True)
        self._parser.add_argument('type1', location='json', help = 'Este campo é obrigatório', required = True)
        self._parser.add_argument('type2', location='json')
        self._parser.add_argument('type3', location='json')

    
class MusicPostParser(Parser, metaclass=ParserMeta):
    def doSetup(self):
        self._parser.add_argument('id', help = 'Este campo é obrigatório', required = True)
        self._parser.add_argument('name')
        self._parser.add_argument('author')
        self._parser.add_argument('type1')
        self._parser.add_argument('type2')
        self._parser.add_argument('type3')

class MusicDeleteParser(Parser, metaclass=ParserMeta):
    def doSetup(self):
        self._parser.add_argument('id', location='json', help = 'Este campo é obrigatório', required = True)
