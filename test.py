import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com/")
page_tile = driver.title
assert "Facebook - Đăng nhập hoặc đăng ký" in page_tile
username = driver.find_element_by_id("email")
username.send_keys("nhập user đúng vào đây")
time.sleep(1)
password = driver.find_element_by_id("pass")
password.send_keys("nhập pass đúng vào đây")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
//*[@id="loginbutton"]