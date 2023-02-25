import requests
from bs4 import BeautifulSoup as BS
import csv


def write_csv(lists: list, file_name: str, delimiter: str):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=delimiter)
        for i in range(len(lists[0])):
            row = [lists[j][i] for j in range(len(lists))]
            writer.writerow(row)


def token_names(html: str, quantity_per_page: int) -> list:
    all_token_names = []
    for i in range(quantity_per_page):
        all_token_names.append(html.select('span.font-bold.tw-items-center.tw-justify-between')[i].text.strip())
    return all_token_names


def token_price(html: str, quantity_per_page: int) -> list:
    all_token_price = []
    for i in range(quantity_per_page):
        all_token_price.append(html.select('div.tw-flex-1 span')[i].text.replace(",", "").replace("$", "").replace(".", ","))
    return all_token_price


def token_1h(html: str, quantity_per_page: int) -> list:
    all_token_h1 = []
    for i in range(quantity_per_page):
        all_token_h1.append(html.select('td.td-change1h.change1h.stat-percent.text-right.col-market span')[i].text)
    return all_token_h1


def token_24h(html: str, quantity_per_page: int) -> list:
    all_token_h2 = []
    for i in range(quantity_per_page):
        all_token_h2.append(html.select('td.td-change24h.change24h.stat-percent.text-right.col-market span')[i].text)
    return all_token_h2


def token_7d(html: str, quantity_per_page: int) -> list:
    all_token_7d = []
    for i in range(quantity_per_page):
        all_token_7d.append(html.select('td.td-change7d.change7d.stat-percent.text-right.col-market span')[i].text)
    return all_token_7d


def trading_volume(html: str, quantity_per_page: int) -> list:
    all_token_volume = []
    for i in range(quantity_per_page):
        all_token_volume.append(html.select('td.td-liquidity_score.lit.text-right.col-market')[i].text.strip().replace(",", "").replace("$", "").replace(".", ","))
    return all_token_volume


def mkt_cap(html: str, quantity_per_page: int) -> list:
    all_token_volume = []
    for i in range(quantity_per_page):
        all_token_volume.append(html.select('td.td-market_cap.cap.col-market.cap-price.text-right span')[i].text.replace(",", "").replace("$", "").replace(".", ","))
    return all_token_volume


last_page = 1
temp = []
for i in range(1, last_page + 1):
    response = requests.get(f"https://www.coingecko.com/?page={i}")
    html = BS(response.content, "html.parser")
    quantity_per_page = len(html.select('span.font-bold.tw-items-center.tw-justify-between'))
    temp.append(["Names"] + token_names(html, quantity_per_page))
    temp.append(["Prices"] + token_price(html, quantity_per_page))
    temp.append(["1h"] + token_1h(html, quantity_per_page))
    temp.append(["24h"] + token_24h(html, quantity_per_page))
    temp.append(["7d"] + token_7d(html, quantity_per_page))
    temp.append(["24h Volume"] + trading_volume(html, quantity_per_page))
    temp.append(["Mkt Cap"] + mkt_cap(html, quantity_per_page))
write_csv(temp, "f1.csv", ";")
