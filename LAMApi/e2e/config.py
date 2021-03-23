import json 

class Config:
    def __init__(self, config_path):
        try:
            f = open(config_path, 'r')
        except:
            raise Exception(f'You must create the config.js at {config_path}.')
        
        data = json.load(f) 
        
        if 'url' not in data:
            raise Exception(f'You must create the "url" parameter on config.js. This parameter will be the url base for testing.')

        if 'login' not in data:
            raise Exception(f'You must create the "login" parameter on config.js. This parameter will be the user login.')

        if 'password' not in data:
            raise Exception(f'You must create the "password" parameter on config.js. This parameter will be the user password.')

        if 'driver_path' not in data:
            raise Exception(f'You must create the "driver_path" parameter on config.js. This parameter will be the path to the selenium Chrome Driver.')

        if 'timeout' not in data:
            raise Exception(f'You must create the "timeout" parameter on config.js. This parameter will be the timeout for waiting procedures.')

        self.url = data['url']
        self.login = data['login'] 
        self.password = data['password']
        self.driver_path = data['driver_path']
        self.timeout = data['timeout']
        
        f.close() 