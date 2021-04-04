from flask_restful.reqparse import RequestParser

import abc


class SingletonMeta(type):
    """The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Possible changes to the value of the `__init__` argument do not affect
        the returned instance.

        Returns:
            self: The unique instance of the class.
        """
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Parser:
    def __init__(self):
        self._parser = RequestParser()

    def getArgs(self):
        return self._parser.parse_args()

    @abc.abstractmethod
    def doSetup(self):
        raise NotImplementedError


class ParserMeta(type):
    """The Parser will obrigatory execute the do Setup for the object.
    """
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        """Possible changes to the value of the `__init__` argument do not affect
        the returned instance.

        Returns:
            self: The parser with setup done.
        """
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            instance.doSetup()
            cls._instances[cls] = instance

        return cls._instances[cls]
