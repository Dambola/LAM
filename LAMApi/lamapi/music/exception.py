class NotValidMusicJSONFormat(Exception):
    def __init__(self):
        super().__init__('Music must be a json type.')

class NotValidMusicJSONName(Exception):
    def __init__(self):
        super().__init__('Name not found in music json.')

class NotValidMusicJSONAuthor(Exception):
    def __init__(self):
        super().__init__('Author not found in music json.')

class NotValidMusicJSONType1(Exception):
    def __init__(self):
        super().__init__('Type 1 not found in music json.')

class NotValidMusicJSONType2(Exception):
    def __init__(self):
        super().__init__('Type 2 not found in music json.')

class NotValidMusicJSONType3(Exception):
    def __init__(self):
        super().__init__('Type 3 not found in music json.')
        