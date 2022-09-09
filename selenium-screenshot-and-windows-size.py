
import selenium
from selenium import webdriver
import time
path = r"D:\chromedriver_win32\chromedriver.exe"

browser = webdriver.Chrome(path)
browser.get("https://teknojoli.com")
title = browser.title
print(title)

browser.set_window_size(250,250)
browser.save_screenshot(r"D:\deneme.png")
#browser.minimize_window()
#browser.maximize_window()
time.sleep(3)
browser.close()  #one tabs close
#browser.quit()  #all tabs close

