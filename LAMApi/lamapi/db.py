import warnings
import pymysql

class DatabaseManager():
    def __init__(self, host, user, password=None, db=None, charset=None):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__db = db
        self.__charset = charset
        self.__connection = None
        warnings.filterwarnings("ignore")

    def connect(self):
        data = {
            'host'        : self.__host,
            'user'        : self.__user,
            'cursorclass' : pymysql.cursors.DictCursor,
        }

        if self.__password:
            data['password'] = self.__password
        if self.__db:
            data['db'] = self.__db
        if self.__charset:
            data['charset'] = self.__charset

        self.__connection = pymysql.connect(**data)
        self.__connection.autocommit(False)

    def select(self, sql, *args):
        with self.__connection.cursor() as cursor:
            cursor.execute(sql % args)
            result = cursor.fetchall()
            return result
    
    def select_one(self, sql, *args):
        with self.__connection.cursor() as cursor:
            cursor.execute(sql % args)
            result = cursor.fetchone()
            return result

    def execute(self, sql, *args):
        with self.__connection.cursor() as cursor:
            cursor.execute(sql, args)

    def begin(self):
        self.__connection.begin() 
        
    def commit(self):
        self.__connection.commit() 
    
    def rollback(self):
        self.__connection.rollback() 

    def affected_rows(self):
        return self.__connection.affected_rows() 
    
    def insert_id(self):
        return self.__connection.insert_id() 

    def close(self):
        self.__connection.close()
        self.__connection = None