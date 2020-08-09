from lamapi import db

# class MusicModel:
#     tablename = 'music'
#     columns = ['id','name','author','type1','type2','type3']
#     columnsTypes = ['int','varchar','int','int','int','int']

#     def __init__(self, name, author, type1, type2=None, type3=None, id=None):
#         self.id = id
#         self.name = name
#         self.author = author
#         self.type1 = type1
#         self.type2 = type2
#         self.type3 = type3

#     def select(self, connection):
#         if not self.id:
#             return False
        
#         SQL =  'SELECT `%s`\n' % ('`, `'.join(MusicModel.columns))
#         SQL += 'FROM `%s`\n' % (MusicModel.tablename)
#         SQL += 'WHERE `id` = %d\n' % (self.id)

#         row = connection.select_one(SQL)
#         if not row:
#             return False
#         self.name = row['name']
#         self.author = row['author']
#         self.type1 = row['type1']
#         self.type2 = row['type2']
#         self.type3 = row['type3']
#         return True

#     def insert(self, connection):
#         if self.id:
#             return False
        
#         SQL =  'INSERT `%s`\n' % (MusicModel.tablename)
#         SQL += '(%s,%s,%s,%s,%s)\n' % ('name','author','type1','type2','type3')
#         SQL += 'VALUES\n'
#         SQL += '(\'%s\',%d,%d,%d,%d)\n' % (self.name,self.author,self.type1,self.type2,self.type3)

#         connection.execute(SQL)
#         new_id = connection.insert_id()

#         if not new_id or new_id <= 0:
#             return False
#         self.id = new_id
#         return True

#     def update(self, connection):
#         if not self.id:
#             return False
        
#         SQL =  'UPDATE `%s`\n' % (MusicModel.tablename)
#         SQL += 'SET\n'
#         SQL += '`name` = \'%s\',\n' % (self.name)
#         SQL += '`author` = %d,\n' % (self.author)
#         SQL += '`type1` = %d,\n' % (self.type1)
#         SQL += '`type2` = %d,\n' % (self.type2)
#         SQL += '`type3` = %d\n' % (self.type3)
#         SQL += 'WHERE `id` = %s\n' % (self.id)

#         connection.execute(SQL)
#         return True

#     def delete(self, connection):
#         if not self.id:
#             return False

#         SQL =  'DELETE\n'
#         SQL += 'FROM `%s`\n' % (MusicModel.tablename)
#         SQL += 'WHERE `id` = %d\n' % (self.id)

#         connection.execute(SQL)
#         return True
        
#     def as_json(self):
#         return {
#             'id'     : self.id,
#             'name'   : self.name,
#             'author' : self.author,
#             'type1'  : self.type1,
#             'type2'  : self.type2,
#             'type3'  : self.type3,
#         }
        
#     @classmethod
#     def query(self, connection, where=None, orderby=None, limit=None):

#         SQL =  'SELECT `%s`\n' % ('`, `'.join(MusicModel.columns))
#         SQL += 'FROM `%s`\n' % (MusicModel.tablename)
#         SQL += 'WHERE %s\n' % where if where else ''
#         SQL += 'ORDER BY %s\n' % orderby if orderby else ''
#         SQL += 'LIMIT %s\n' % limit if limit else ''

#         return [
#             MusicModel(
#                 row['name'],
#                 row['author'],
#                 row['type1'],
#                 type2=row['type2'],
#                 type3=row['type3'],
#                 id=row['id']
#             ) for row in connection.select(SQL)
#         ]

#     @classmethod
#     def createTable(self, connection):
#         connection.execute("drop table %s" % self.tablename)
#         connection.execute(MUSIC_SQL_TABLE_CREATE)

#     @classmethod
#     def checkTable(self, connection):
#         colInfo = { key:value for key, value in zip(MusicModel.columns,MusicModel.columnsTypes) }
#         rows = connection.select(MUSIC_SQL_TABLE_COLUMNS,DATABASE_SCHEMA)
#         cnt = 0
#         for row in rows:
#             column_name = row['COLUMN_NAME']
#             column_type = row['DATA_TYPE']
#             if column_name not in colInfo or \
#                 colInfo[column_name] != column_type:
#                 return False
#             cnt += 1
#         if len(colInfo) != cnt:
#             return False
#         return True

#     def __str__(self):
#         return 'Music(%s,%s,%s,%s,%s)' % \
#             (self.name,self.author,self.type1,self.type2,self.type3)

#     def __repr__(self):
#         return '<Music %r>' % (self.name)


class MusicModel(db.Model):
    __tablename__ = 'musics'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100), nullable = False)
    author = db.Column(db.Integer, nullable = False)
    type1 = db.Column(db.Integer, nullable = False)
    type2 = db.Column(db.Integer, nullable = True)
    type3 = db.Column(db.Integer, nullable = True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()