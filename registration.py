#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
import time 
import os

def openFile(log):
    os.startfile('C:\\Users\\Aleksandr\\Desktop\\register test.txt')
log = open('C:\\Users\\Aleksandr\\Desktop\\register test.txt', 'w')
link = "https://planoplan.com" 
browser = webdriver.Chrome()
browser.get(link)
#Регистрация нового пользователя на странице planoplan.com
try:
    browser.implicitly_wait(10) #искать каждый элемент в течение 5 секунд
    browser.get(link)
    login = browser.find_element_by_css_selector('[data-template="#login_box"]') #ищем кнопку "Войти"
    login.click()
    agree = browser.find_element_by_id('register_inpopup') #ищем кнопку "зарегистрироваться"
    agree.click()
    name = browser.find_element_by_id('register_name')
    name.send_keys('Тестер')
    mail = browser.find_element_by_id('register_mail')
    mail.send_keys('tests_one@planoplan.com')
    password = browser.find_element_by_id('register_pass')
    password.send_keys('121212')
    rules = browser.find_element_by_id('register_apply_rules')
    rules.click()
    register = browser.find_element_by_css_selector('[class="style_button_base style_button disabled"]')
    log.write('Тест "Регистрация нового пользователя на странице planoplan.com". Пройден' + '\n')
except:
    log.write('Тест "Регистрация нового пользователя на странице planoplan.com". Провален' + '\n')
finally:
    browser.quit() #закрываем браузер после всех манипуляций
#Регистрация нового пользователя на странице planoplan.com/demo
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(60) #искать каждый элемент в течение 5 секунд
    points = browser.find_element_by_class_name('newpp_header__menu-item.newpp_header__menu-submenu-toggle')
    points.click()
    demo = browser.find_element_by_css_selector('[href="/ru/demo/"]')
    demo.click()
    browser.switch_to.frame(browser.find_element_by_id('editor'))
    further = browser.find_element_by_class_name('sc-dymIpo.jxGjhs')
    further.click()
    further.click()
    save = browser.find_element_by_class_name('sc-cmTdod.dxcgL')
    save.click()
    mail = browser.find_element_by_id('regEmail')
    mail.send_keys('tester@planoplan.com')
    password = browser.find_element_by_id('regPassword')
    password.send_keys('123456')
    agree = browser.find_element_by_id('reg-agreement')
    agree.click()
    button = browser.find_element_by_xpath('//form[@class="sc-bsbRJL jFQzBz"]/button')
    button_allright = button.get_attribute('disabled')
    assert button_allright is None
    log.write('Тест "Регистрация нового пользователя на странице planoplan.com/demo". Пройден' + '\n')
except:
    log.write('Тест "Регистрация нового пользователя на странице planoplan.com/demo". Провален' + '\n')
finally:
    browser.quit() #закрываем браузер после всех манипуляций
#Регистрация нового пользователя на странице planoplan.com/ru/pricicng
try:
    browser = webdriver.Chrome()
    browser.get('https://planoplan.com')
    browser.implicitly_wait(10) #искать каждый элемент в течение 10 секунд
    time.sleep(2.0)
    pricing = browser.find_element_by_xpath('//a[@href="/ru/pricing/"]')
    pricing.click()

    registration = browser.find_element_by_css_selector('[data-template="#register_box"]')
    registration.click()
    name = browser.find_element_by_id('register_name')
    name.send_keys('Test')
    mail = browser.find_element_by_id('register_mail')
    mail.send_keys('tester@planoplan.com')
    password = browser.find_element_by_id('register_pass')
    password.send_keys('124356')
    agree = browser.find_element_by_id('register_apply_rules')
    agree.click()
    button = browser.find_element_by_id('register_submit')
    button_allright = button.get_attribute('disabled')
    assert button_allright is None
    log.write('Тест "Регистрация нового пользователя на странице planoplan.com/ru/pricicng". Пройден' + '\n')
except:
    log.write('Тест "Регистрация нового пользователя на странице planoplan.com/ru/pricing". Провален' + '\n')
finally:
    browser.quit()# закрываем браузер после всех манипуляций
#Переход на страницу магазина при клике "Купить" ТП Pro, пользователь создан.
try:
    browser = webdriver.Chrome()
    browser.get('https://planoplan.com/ru/pricing/')
    browser.implicitly_wait(30) #искать каждый элемент в течение 10 секунд
    login = browser.find_element_by_css_selector('[href="#login"]')
    login.click()
    mail = browser.find_element_by_id('login_mail')
    mail.send_keys('alkawtan@gmail.com')
    password = browser.find_element_by_id('login_pass')
    password.send_keys('123456')
    agree = browser.find_element_by_id('agreementSocial')
    agree.click()
    button = browser.find_element_by_id('login_submit')
    button.click()
    time.sleep(2.0) #ждём, пока подгрузится страница (иначе ссылку на страницу с тарифами не нажать)
    pricing = browser.find_element_by_xpath('//a[@href="/ru/pricing/"]')
    pricing.click()
    go = browser.find_element_by_css_selector('[href="/ru/cabinet/tariff-managment/?tariff=2"]')
    go.click()
    tp = browser.find_element_by_class_name('header__Name-nlm80s-3.cBGuKJ')
    if tp.text == 'PRO':
        log.write('Тест "Переход на страницу магазина при клике "Купить" ТП Pro, пользователь создан". Пройден' + '\n')
    else:
        log.write('Тест "Переход на страницу магазина при клике "Купить" ТП Pro, пользователь создан". Провален' + '\n')
except:
    pass
finally:
    browser.quit()# закрываем браузер после всех манипуляций

openFile(log)
log.close()
 #не забываем оставить пустую строку в конце файла