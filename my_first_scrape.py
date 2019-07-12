from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, 'html.parser')
# grabs each product
containers = page_soup.findAll("div", {'class':'item-info'})

filename = 'products.csv'
f = open(filename, 'w')

headers = 'product_name, price, shipping\n'

f.write(headers)

for container in containers:
	

	title_container = container.findAll('a', {'class':'item-title'})
	product_name = title_container[0].text

	price_container = container.findAll('li', {'class':'price-current'})
	price = price_container[0].text
	current_price = price[price.find('$'):price.find('\xa0')]

	shipping_container = container.findAll('li',{'class':'price-ship'})
	shipping = shipping_container[0].text.strip()


	
	print('product_name: ' + product_name)
	print('price: ' + current_price)
	print('shipping: ' + shipping)

	f.write(product_name.replace(',', '|')+',' +current_price.replace(',','')+','+ shipping +'\n')

f.close()