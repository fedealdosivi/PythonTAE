from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com.ar/")
driver.find_element_by_name("q").send_keys("Hola")
driver.find_element_by_class_name("gb_b gb_dc").click()