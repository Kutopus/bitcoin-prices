import time
import requests
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from time import gmtime, strftime

page = requests.get("https://coinmarketcap.com/pt-br/currencies/bitcoin/")

soup = BeautifulSoup(page.content, 'html.parser')

divs = soup.find_all("div", {"class": "priceValue smallerPrice"})

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
values = []
z = 0

while z != 10:
    for tag in divs:
        print(strftime("%d-%m-%Y %H:%M:%S", gmtime()), ": ", tag.text.strip())
        tag = str(tag.text)
        tag = tag[2:]
        tag = tag.replace(",", "")
        tag = float(tag)
        values.append(tag)
        time.sleep(0.1)
        z += 1

plt.plot(x, values)
plt.show()
