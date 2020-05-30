from lamapi.models.sql import MUSIC_SQL_TABLE_CREATE, MUSIC_SQL_TABLE_COLUMNS
from lamapi.config import DATABASE_SCHEMA

class MusicModel:
    tablename = 'music'
    columns = ['id','name','author','type1','type2','type3']
    columnsTypes = ['int','varchar','int','int','int','int']

    def __init__(self, name, author, type1, type2=None, type3=None, id=None):
        self.id = id
        self.name = name
        self.author = author
        self.type1 = type1
        self.type2 = type2
        self.type3 = type3

    def select(self, database):
        if not self.id:
            return False
        
        SQL =  'SELECT `%s`\n' % ('`, `'.join(MusicModel.columns))
        SQL += 'FROM `%s`\n' % (MusicModel.tablename)
        SQL += 'WHERE `id` = %d\n' % (self.id)

        row = database.select_one(SQL)
        if not row:
            return False
        self.name = row['name']
        self.author = row['author']
        self.type1 = row['type1']
        self.type2 = row['type2']
        self.type3 = row['type3']
        return True

    def insert(self, database):
        if self.id:
            return False
        
        SQL =  'INSERT `%s`\n' % (MusicModel.tablename)
        SQL += '(%s,%s,%s,%s,%s)\n' % ('name','author','type1','type2','type3')
        SQL += 'VALUES\n'
        SQL += '(\'%s\',%d,%d,%d,%d)\n' % (self.name,self.author,self.type1,self.type2,self.type3)

        database.execute(SQL)
        new_id = database.insert_id()

        if not new_id or new_id <= 0:
            return False
        self.id = new_id
        return True

    def update(self, database):
        if not self.id:
            return False
        
        SQL =  'UPDATE `%s`\n' % (MusicModel.tablename)
        SQL += 'SET\n'
        SQL += '`name` = \'%s\',\n' % (self.name)
        SQL += '`author` = %d,\n' % (self.author)
        SQL += '`type1` = %d,\n' % (self.type1)
        SQL += '`type2` = %d,\n' % (self.type2)
        SQL += '`type3` = %d\n' % (self.type3)
        SQL += 'WHERE `id` = %s\n' % (self.id)

        database.execute(SQL)
        return True

    def delete(self, database):
        if not self.id:
            return False

        SQL =  'DELETE\n'
        SQL += 'FROM `%s`\n' % (MusicModel.tablename)
        SQL += 'WHERE `id` = %d\n' % (self.id)

        database.execute(SQL)
        return True
        
    def as_json(self):
        return {
            'id'     : self.id,
            'name'   : self.name,
            'author' : self.author,
            'type1'  : self.type1,
            'type2'  : self.type2,
            'type3'  : self.type3,
        }
        
    @classmethod
    def query(self, database, where=None, orderby=None, limit=None):

        SQL =  'SELECT `%s`\n' % ('`, `'.join(MusicModel.columns))
        SQL += 'FROM `%s`\n' % (MusicModel.tablename)
        SQL += 'WHERE %s\n' % where if where else ''
        SQL += 'ORDER BY %s\n' % orderby if orderby else ''
        SQL += 'LIMIT %s\n' % limit if limit else ''

        return [
            MusicModel(
                row['name'],
                row['author'],
                row['type1'],
                type2=row['type2'],
                type3=row['type3'],
                id=row['id']
            ) for row in database.select(SQL)
        ]

    @classmethod
    def createTable(self, database):
        database.execute("drop table %s" % self.tablename)
        database.execute(MUSIC_SQL_TABLE_CREATE)

    @classmethod
    def checkTable(self, database):
        colInfo = { key:value for key, value in zip(MusicModel.columns,MusicModel.columnsTypes) }
        rows = database.select(MUSIC_SQL_TABLE_COLUMNS,DATABASE_SCHEMA)
        cnt = 0
        for row in rows:
            column_name = row['COLUMN_NAME']
            column_type = row['DATA_TYPE']
            if column_name not in colInfo or \
                colInfo[column_name] != column_type:
                return False
            cnt += 1
        if len(colInfo) != cnt:
            return False
        return True

    def __str__(self):
        return 'Music(%s,%s,%s,%s,%s)' % \
            (self.name,self.author,self.type1,self.type2,self.type3)

    def __repr__(self):
        return '<Music %r>' % (self.name)
