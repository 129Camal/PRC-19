import bs4
from urllib.request import urlopen as request
from bs4 import BeautifulSoup as soup

my_url = "https://dataride.uci.ch/Results/iframe/EventResults/181231?competitionId=57048&disciplineId=10"

client = request(my_url)

page_html = client.read()

client.close()

page_soup = soup(page_html, "html.parser")

print(page_soup)
#page_soup = page_soup

# containers = page_soup.findAll("div", {"class": "t-gmg-brands-menu-inner js-gmg-brands-menu-content"})

# for container in containers:
#     lis = container.findAll("ul")
    
#     for li in lis:
#         li = li.findAll("li")
#         #print(li)
#         for item in li:
#             print("Link: " + str(item.a["href"]) + "\nNome: " + str(item.a.span.text) )