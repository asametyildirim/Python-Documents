import selenium
from selenium import webdriver
import time
path = r"D:\chromedriver_win32\chromedriver.exe"

browser = webdriver.Chrome(path)
browser.get("https://www.sahibinden.com")
time.sleep(2)


browser.set_window_size(1280,720)
browser.execute_script("window.scrollTo(0,500)")

click_the_close = browser.find_element("xpath",'//*[@id="onetrust-accept-btn-handler"]')
click_the_close.click()
time.sleep(1)
click_the_div = browser.find_element("xpath",'//*[@id="container"]/div[3]/div/aside/div[1]/nav/ul[4]/li[2]/ul/li[1]/a')
click_the_div.click()
time.sleep(2)

click_the_bmw = browser.find_element("xpath",'//*[@id="container"]/div/div[1]/div[1]/div[2]/ul/div/div[1]/li[8]/a')
click_the_bmw.click()
time.sleep(2)

browser.execute_script("window.scrollTo(0,750)")
click_the_selector = browser.find_element("xpath",'//*[@id="searchResultLeft-a17"]/dl/dd/ul/div/div/li[1]/div/a')
click_the_selector.click()

click_the_search = browser.find_element("xpath",'//*[@id="searchResultsSearchForm"]/div/div[3]/div[24]/button')
click_the_search.click()

browser.save_screenshot(r"D:\cars.png")

time.sleep(25)
browser.close()
browser.quit()  #all tabs close

