import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Turtle-Gaming-Headset-PlayStation-Nintendo-Console/dp/B00YXO5U40/ref=sr_1_1?_encoding=UTF8&sr=8-1"
response = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36","Accept-Language":"en-US,en;q=0.7"})
daraz_headphone = response.text
soup = BeautifulSoup(daraz_headphone, "lxml")
price_html= soup.select_one("#color_name_1_price span")
price_tag = price_html.getText()
lis = price_tag.split("$")
print(lis)
price =  float(lis[1])
if price<20:
    print("Hey, you got your price lowered to $20")
else:
    print("Hey, the price is the same")