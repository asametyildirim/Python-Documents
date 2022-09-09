import selenium
from selenium import webdriver
path = r"D:\chromedriver_win32\chromedriver.exe"

browser = webdriver.Chrome(path)
browser.get("https://teknojoli.com")
