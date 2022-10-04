import time
from selenium.webdriver.common.by import By
from selenium import webdriver
# import selenium
# print(selenium.__version__)
'''
User Name: Lmaras           
P/W: 2022Gazprom2!
'''

'''
Points from trainner:
    
'''

prefs = {'download.default_directory': "/home/hrudratt/Hrudratt/Files"}
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path='/home/hrudratt/Hrudratt/chromedriver_linux64/chromedriver', options=options)
driver.maximize_window()
driver.get("https://gtsnext.pge.com/gts")
time.sleep(5)
driver.find_element("xpath", '''//input[@id="username"]''').send_keys('Lmaras')
driver.find_element(By.XPATH, '''//input[@id="username"]/parent::*/following-sibling::*//input[contains(@*,'password')]''').send_keys('2022Gazprom2!')
driver.find_element(By.XPATH, '''//button[contains(text(),'Log In')]''').click()
time.sleep(2)
driver.find_element(By.XPATH, '''//*[@id="header"]//*[contains(text(),'Nominations')]''').click()
time.sleep(1)
driver.find_element(By.XPATH, '''//*[contains(text(),'Query Nomination Details')]''').click()
time.sleep(2)
enter_date = driver.find_element(By.XPATH, '''//input[@id="gasDayID"]''')
enter_date.clear()
enter_date.send_keys('09/25/2022')
time.sleep(1)
driver.find_element(By.XPATH, '''//*[@class="submit"]/button[contains(text(),'Query')]''').click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.XPATH, '''//*[contains(text(),'Export option')]//*[contains(text(),'CSV')]/parent::*''').click()
time.sleep(5)
driver.close()
driver.quit()
print()
