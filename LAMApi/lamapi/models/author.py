from lamapi.models.sql import AUTHOR_SQL_TABLE_CREATE

class AuthorModel:
    tablename = 'author'
    columns = ['id','name']

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def update(self, connection):
        if not self.id:
            return False
        
        SQL =  'UPDATE `%s`\n' % (AuthorModel.tablename)
        SQL += 'SET\n'
        SQL += '`name` = \'%s\',\n' % (self.name)
        SQL += 'WHERE `id` = %s\n' % (self.id)

        connection.execute(SQL)
        return True

    def insert(self, connection):
        if self.id:
            return False
        
        SQL =  'INSERT `%s`\n' % (AuthorModel.tablename)
        SQL += '(%s)\n' % ('name')
        SQL += 'VALUES\n'
        SQL += '(\'%s\')\n' % (self.name)

        connection.execute(SQL)
        new_id = connection.insert_id()

        if not new_id or new_id <= 0:
            return False
        self.id = new_id
        return True
    
    def as_json(self):
        return {
            'id'     : self.id,
            'name'   : self.name
        }
        
    @classmethod
    def query(self, connection, where=None, orderby=None):
        if isinstance(where, list):
            where = ' AND '.join(where)
        if isinstance(orderby, list):
            orderby = ', '.join(orderby)

        SQL =  'SELECT `%s`\n' % ('`, `'.join(AuthorModel.columns))
        SQL += 'FROM `%s`\n' % (AuthorModel.tablename)
        SQL += 'WHERE %s\n' % where if where else ''
        SQL += 'ORDER BY %s\n' % orderby if orderby else ''

        return [
            AuthorModel(
                row['name'],
                id=row['id']
            ) for row in connection.select(SQL)
        ]

    @classmethod
    def createTable(self, connection):
        connection.execute(AUTHOR_SQL_TABLE_CREATE)

    def __str__(self):
        return 'Type(%s)' % (self.name)

    def __repr__(self):
        return '<Type %r>' % (self.name)
