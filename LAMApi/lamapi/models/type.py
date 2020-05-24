from lamapi.models.sql import TYPE_SQL_TABLE_CREATE

class TypeModel:
    tablename = 'type'
    columns = ['id','name']

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def update(self, database):
        if not self.id:
            return False
        
        SQL =  'UPDATE `%s`\n' % (TypeModel.tablename)
        SQL += 'SET\n'
        SQL += '`name` = \'%s\',\n' % (self.name)
        SQL += 'WHERE `id` = %s\n' % (self.id)

        database.execute(SQL)
        return True

    def insert(self, database):
        if self.id:
            return False
        
        SQL =  'INSERT `%s`\n' % (TypeModel.tablename)
        SQL += '(%s)\n' % ('name')
        SQL += 'VALUES\n'
        SQL += '(\'%s\')\n' % (self.name)

        database.execute(SQL)
        new_id = database.insert_id()

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
    def query(self, database, where=None, orderby=None):
        if isinstance(where, list):
            where = ' AND '.join(where)
        if isinstance(orderby, list):
            orderby = ', '.join(orderby)

        SQL =  'SELECT `%s`\n' % ('`, `'.join(TypeModel.columns))
        SQL += 'FROM `%s`\n' % (TypeModel.tablename)
        SQL += 'WHERE %s\n' % where if where else ''
        SQL += 'ORDER BY %s\n' % orderby if orderby else ''

        return [
            TypeModel(
                row['name'],
                id=row['id']
            ) for row in database.select(SQL)
        ]

    @classmethod
    def createTable(self, database):
        database.execute(TYPE_SQL_TABLE_CREATE)

    def __str__(self):
        return 'Type(%s)' % (self.name)

    def __repr__(self):
        return '<Type %r>' % (self.name)
