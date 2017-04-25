import requests
from bs4 import BeautifulSoup


def get_html(url):
    raw_html=requests.get(url)
    return raw_html.text

def get_links(html):
    soup = BeautifulSoup(html, "lxml")

    items = soup.find("div", class_="list-items").find_all("div", class_= "list-item")
    links = []
    for item in items:
        try:
            # print(item.text)
            a = item.find("a").get("href")
            a_full = "https://morepiva.ua" + a
            links.append(a_full)
        except:
            print("chto to poshlo ne tak")
    return links

def get_quant(html):
    soup = BeautifulSoup(html, "lxml")
    shops = soup.find("div", id="stores-amount").find_all("li")
    # print (shops)
    shop_list = []
    sh_qu = [3]
    for shop in shops:
        a = shop.find("span").get_text().split()
        b = shop.find("div", class_="amount").get("data-quantity").split(".")
        shop_list.append((a[1],b[0]))

    return shop_list

def main():
    url = "https://morepiva.ua/kyiv/pivo/?PAGEN_1=2"
    # url2 = "https://morepiva.ua/kyiv/pivo/pivo-kronenburg-blansh.html"
    links_all = get_links(get_html(url))
    # quants = get_quant(get_html(url2))
    for links in links_all:
        print(links)
    # for quant in quants:
    #     print(quant)

if __name__ == "__main__":
    main()
