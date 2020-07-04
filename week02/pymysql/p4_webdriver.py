from selenium import webdriver

import time

from selenium.webdriver.chrome.webdriver import WebDriver

try:
    browser: WebDriver = webdriver.Chrome()
    browser.get('https://www.douban.com')
    time.sleep(1)

    browser.switch_to_frame(browser.find_element_by_tag_name('iframe'))
    btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    btm1.click()

    browser.find_element_by_xpath('//*[@id="username"]').send_keys("15001787927")
    browser.find_element_by_id('password').send_keys('Zhangyi!!178')
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)
except Exception as e:
    print(e)
finally:
    browser.close()