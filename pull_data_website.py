import requests
from lxml.html import fromstring

HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', \
                'Accept-Language': 'en-US, en;q=0.5'})
r = requests.get('https://www.reddit.com/r/AskReddit/comments/yaqpzk/what_is_a_cult_that_pretends_its_not_cult/',
                     headers=HEADERS)

source = fromstring(r.text)

title = source.xpath('//*[@id="t3_yaqpzk"]/div/div[3]/div[1]/div/h1')


print(title[0].text)