import selenium
from selenium import webdriver
import time
path = r"D:\chromedriver_win32\chromedriver.exe"

browser = webdriver.Chrome(path)
browser.get("https://teknojoli.com")
time.sleep(2)

click_the_div = browser.find_element("xpath",'//*[@id="pgc-3645-0-0"]/div/div/div/div[1]/div/div/h3/a')
time.sleep(2)
browser.execute_script("window.scrollTo(0,300)")
click_the_div.click()



time.sleep(25)
browser.quit()  #all tabs close

