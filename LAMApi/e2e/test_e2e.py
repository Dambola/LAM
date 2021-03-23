from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from e2e import config
from e2e.utils import do_login

def test_login(selenium):
    do_login(selenium, config)
    condition = EC.presence_of_element_located((By.ID, 'welcome-home-title'))
    e_title = WebDriverWait(selenium, config.timeout).until(condition)
    assert e_title.text.strip() == 'Bem vindo ao LAM!'

def test_tab_click(selenium):
    do_login(selenium, config)
    condition = EC.presence_of_element_located((By.ID, 'welcome-home-title'))
    e_title = WebDriverWait(selenium, config.timeout).until(condition)

    clicks_done = True

    def doClickOnTab(selector):
        try:
            condition = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            element = WebDriverWait(selenium, config.timeout).until(condition)
            element.click()
            return True
        except:
            return False
    
    clicks_done &= doClickOnTab('a[href$="/indicacao"]')
    clicks_done &= doClickOnTab('a[href$="/musica"]')
    clicks_done &= doClickOnTab('a[href$="/relatorio"]')
    clicks_done &= doClickOnTab('a[href$="/admin"]')
    clicks_done &= doClickOnTab('a[href$="/perfil"]')
    clicks_done &= doClickOnTab('a[href$="/"]')

    assert clicks_done

def test_music_table_exist(selenium):
    do_login(selenium, config)
    condition = EC.presence_of_element_located((By.ID, 'welcome-home-title'))
    e_title = WebDriverWait(selenium, config.timeout).until(condition)

    selenium.find_elements_by_css_selector('a[href="#/musica"]')[0] \
        .click()

    condition = EC.presence_of_element_located((By.CSS_SELECTOR, 'table.q-table'))
    e_table = WebDriverWait(selenium, config.timeout).until(condition)
    assert e_table
