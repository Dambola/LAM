from setuptools import setup
import os 

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Louvor Agape Montese API",
    version = "1.0.0",
    author = "Daniel Nogueira Rebouças",
    author_email = "danielnreboucas@hotmail.com",
    description = ("The API for Louvor Agape Montese Client."),
    packages=[
        'lamapi',
        'lamapi/models',
        'lamapi/controllers'
    ],
    long_description=read('README')
)