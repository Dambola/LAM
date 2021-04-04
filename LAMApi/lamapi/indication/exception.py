class NotValidIndicationJSONFormat(Exception):
    def __init__(self):
        super().__init__('Indication must be a json type.')

class NotValidIndicationJSONName(Exception):
    def __init__(self):
        super().__init__('Name not found in indication json.')

class NotValidIndicationJSONAuthor(Exception):
    def __init__(self):
        super().__init__('Author not found in indication json.')

class NotValidIndicationJSONType1(Exception):
    def __init__(self):
        super().__init__('Type 1 not found in indication json.')

class NotValidIndicationJSONType2(Exception):
    def __init__(self):
        super().__init__('Type 2 not found in indication json.')

class NotValidIndicationJSONType3(Exception):
    def __init__(self):
        super().__init__('Type 3 not found in indication json.')

class NotValidIndicationJSONUser(Exception):
    def __init__(self):
        super().__init__('User not found in indication json.')

class NotValidIndicationJSONLink(Exception):
    def __init__(self):
        super().__init__('Link not found in indication json.')

class IndicationNotFound(Exception):
    def __init__(self):
        supe().__init__('Indication not found.')

class IndicationNotDeleted(Exception):
    def __init__(self):
        supe().__init__('Indication not deleted.')