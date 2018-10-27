from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/global/in-en/Product/ProductList.aspx?Submit=ENE&Depa=0&Order=BESTMATCH&Description=graphics%20card&IsRelated=1&cm_sp=KeywordRelated-_-graphic_cards-_-graphics%20card"

# open up page and download/grab the page
uClient = uReq(my_url)

page_html = uClient.read()
uClient.close()


# html parsing
page_soup = soup(page_html, "html.parser")
# grabs the item
containers = page_soup.findAll("div",{"class": "item-container"})

filename = "product.csv"
f = open(filename, "w")

headers = "brand, product_name, current_price\n"
f.write(headers)


for container in containers:

    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    # price_Was_container = container.findAll("li", {"class": "price-was"})
    # old_price = price_Was_container[0].span.text.strip()

    price_is_container = container.findAll("li", {"class": "price-current"})
    current_price = price_is_container[0].text.strip()
    current_price = current_price .replace("\xa0\r\n            \n–", "")


    print("brand: "+brand)
    print("product_name: "+product_name)
    # print("old_price"+old_price)
    print("current_price: "+current_price)

    f.write(brand + ","+product_name.replace(",", "|") + "," + current_price + "\n")

f.close()


