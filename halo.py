import requests
from bs4 import BeautifulSoup

halo = requests.get("https://www.halowaypoint.com/en-us/esports/standings")

page = BeautifulSoup(halo.content, "html.parser")

table = page.select_one("div.table.table--hcs")
print(", ".join([td.text for td in table.select("header div.td")]))
for row in table.select("div.tr"):
    rank,team = row.select_one("span.numeric--medium.hcs-trend-neutral").text,row.select_one("div.td.hcs-title").span.a.text
    wins, losses = [div.span.text for div in row.select("div.td.em-7")]
    print(rank,team, wins, losses)