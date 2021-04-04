class OrderBy(object):
    class Id(object):
        Asc = 'id'
        Desc = 'id desc'

    class Name(object):
        Asc = 'name'
        Desc = 'name desc'

    class Author(object):
        Asc = 'author'
        Desc = 'author desc'
    
    class Type(object):
        Asc = 'type'
        Desc = 'type desc'

class FilterBy(object):
    class Key:
        Name = 'name'
        Author = 'author'
        Type = 'type'

    @classmethod
    def Name(cls, *args):
        return { 'key': cls.Key.Name, 'values': args }
    
    @classmethod
    def Author(cls, *args):
        return { 'key': cls.Key.Author, 'values': args }

    @classmethod
    def Type(cls, *args):
        return { 'key': cls.Key.Type, 'values': args }
        