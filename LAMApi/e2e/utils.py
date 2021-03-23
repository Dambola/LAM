def do_login(selenium, config):
    selenium.get(config.url)

    selenium.find_element_by_name('login') \
        .send_keys(config.login)
    selenium.find_element_by_name('password') \
        .send_keys(config.password)
    selenium.find_element_by_name('entrar') \
        .click()