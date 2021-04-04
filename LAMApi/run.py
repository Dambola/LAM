from lamapi import createApplication


if __name__ == '__main__':
    app = createApplication('lamapi.config.LAMConfiguration')
    app.run(host='localhost', port=8390, debug=True)