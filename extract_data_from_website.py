import sys
import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.teknojoli.com/")
if r.status_code == 200:
    print("you can extract data from website")
else:
    print("you can't extract data from website")

#print(r.content)
#print(r.text)
#print(r.encoding)

soup = BeautifulSoup(r.content,"html.parser")
#print(soup.prettify())

write = soup.find_all("p")
#print(write)
""" 
for i in write:
    print(i.text)
    print("-"*25)
"""
get_div = soup.find("h3",{"class":"feature-post-title"}).a.text
print(get_div)


































