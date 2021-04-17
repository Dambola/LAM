from lamapi import createApplication
app = createApplication('lamapi.config.LAMConfiguration')

if __name__ == '__main__':
    app.run(port=8390)