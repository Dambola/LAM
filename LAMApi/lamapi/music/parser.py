from flask_restful.reqparse import RequestParser

class MusicPutParser(object):
    parser = RequestParser()
    parser.add_argument('name', help = 'Este campo é obrigatório', required = True)
    parser.add_argument('author', help = 'Este campo é obrigatório', required = True)
    parser.add_argument('type1', help = 'Este campo é obrigatório', required = True)
    parser.add_argument('type2')
    parser.add_argument('type3')

    @classmethod
    def getArgs(cls):
        return cls.parser.parse_args()

    
class MusicPostParser(object):
    parser = RequestParser()
    parser.add_argument('id', help = 'Este campo é obrigatório', required = True)
    parser.add_argument('name')
    parser.add_argument('author')
    parser.add_argument('type1')
    parser.add_argument('type2')
    parser.add_argument('type3')

    @classmethod
    def getArgs(cls):
        return cls.parser.parse_args()