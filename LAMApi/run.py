from lamapi.controllers import *
from lamapi import api, app, db

api.add_resource(AuthController, '/auth')
api.add_resource(MusicController, '/music')
api.add_resource(TypeController, '/type')
api.add_resource(PermissionController, '/permission')

if __name__ == '__main__':
    app.run(host='localhost', port=8390, debug=True)