from lamapi.controllers import *
from lamapi import api, app, db
from lamapi.models.music import MusicModel

api.add_resource(MusicList, '/music')
api.add_resource(Music, '/music/<int:id>')


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8081,debug=True)