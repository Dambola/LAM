from lamapi.setup import createApplication

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from lamapi.auth import *
from lamapi.indication import *
from lamapi.music import *
from lamapi.permission import *
from lamapi.type import *