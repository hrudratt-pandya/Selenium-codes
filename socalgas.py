import time
from selenium.webdriver.common.by import By

from selenium import webdriver

'''
Points from trainner:

'''


prefs = {'download.default_directory': "/home/hrudratt/Hrudratt/Files"}
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path='/home/hrudratt/Hrudratt/chromedriver_linux64/chromedriver', options=options)
driver.maximize_window()
driver.get("https://socalgas-envoy.com/WebDispatch/ShowLogin.showLogin")
# a = driver.page_source
# time.sleep(2)
# driver.find_element(By.XPATH, '''//*[@id="loginButtonOverlayDesktop"]//*[contains(@name,'LogInButton')]/parent::a''').click()
# time.sleep(3)
# next_tab = driver.window_handles[1]
# driver.switch_to.window(next_tab)
userid = driver.find_element(By.XPATH, '''//input[@name="userid"]''')
userid.send_keys('gs2lmara')
driver.find_element(By.XPATH, '''//input[@name="password"]''').send_keys('Gazprom17')
time.sleep(1)
driver.find_element(By.XPATH, '''//button[@class="button"]''').click()
time.sleep(3)
# next_tab = driver.window_handles[1]
# driver.switch_to.window(next_tab)
driver.execute_script("window.scrollTo(0,250)")
time.sleep(2)
read_mores = driver.find_element(By.XPATH, '''//*[contains(text(), 'Transaction Ledger')]''')
read_mores.click()
time.sleep(2)
start_date = driver.find_element(By.XPATH, '''//input[@name="startDate"]''')
# start_date.click()
start_date.clear()
start_date.send_keys('09/25/2022')
end_date = driver.find_element(By.XPATH, '''//input[@name="endDate"]''')
# end_date.click()
end_date.clear()
end_date.send_keys('09/27/2022')
# try:
driver.find_element(By.XPATH, '''//*[@name="cycleToggleBtn" and contains(text(),'ALL')]''').click()
# except:
#     ...
# try:
driver.find_element(By.XPATH, '''//*[@name="cycleToggleBtn" and contains(text(),'NONE')]''').click()
# except:
#     ...
time.sleep(20)
driver.find_element(By.XPATH, '''//label[contains(.,'Intraday-4')]/input''').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.find_element(By.XPATH, '''//button[contains(text(),'Submit')]''').click()
time.sleep(2)
driver.find_element(By.XPATH, '''//*[@title="Export Transaction"]''').click()
time.sleep(2)
file_name = driver.find_element(By.XPATH, '''//*[contains(text(),'File Name:')]/parent::*//input[@name="FileName"]''')
file_name.clear()
file_name.send_keys('MY_file')
driver.find_element(By.XPATH, '''//form//button[contains(text(),'Export')]''').click()
time.sleep(5)
driver.close()
driver.quit()
print()
