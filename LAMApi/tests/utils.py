def doLogin(client, username, password):
    response = client.post('/auth', data=dict(
            login=username,
            password=password
        ), follow_redirects=True)
    assert response.status_code == 200 