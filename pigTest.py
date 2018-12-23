from selenium import webdriver

driver = webdriver.Firefox(executable_path=r"C:\test\driver\geckodriver.exe")
driver.get("http://www.google.com")
driver.maximize_window()

search = driver.find_element_by_name('q')
search.send_keys('pigs')
FindInGoogle = driver.find_element_by_name('btnI')
FindInGoogle.click()

title = driver.title

driver.close()
