from lamapi.controllers import *
from lamapi import api, app, db
from lamapi.models.music import MusicModel

api.add_resource(MusicGeneralController, '/music')
api.add_resource(MusicController, '/music/<int:id>')


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8081,debug=True)