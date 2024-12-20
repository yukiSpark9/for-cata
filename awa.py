import requests
from bs4 import BeautifulSoup
import re
from tabulate import tabulate

# Example URL for PriceSpy product
urlList = ["https://pricespy.co.nz/product.php?p=13951156",
           "https://pricespy.co.nz/product.php?p=7561365",
           "https://pricespy.co.nz/product.php?p=13644258",
           "https://pricespy.co.nz/product.php?p=12452773",
           "https://pricespy.co.nz/product.php?p=7280452",
           "https://pricespy.co.nz/product.php?p=7153883",
           "https://pricespy.co.nz/product.php?p=12568329",
           "https://pricespy.co.nz/product.php?p=4814030"
           ]
productList, pricelist, wawa = [], [], []
# Send a GET request to the URL
for url in urlList:
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the price using an appropriate tag and class. You'll need to inspect the page for this.
        # Example: Look for a price in a div with class 'product-price'
        name = soup.find('h1', class_=re.compile("StyledDesktopTitle"))  # Adjust this to match the correct class/tag
        productList.append(name.text)
        
        #===================================== price ===============================
        price = soup.find_all(['span', 'h4'], class_=re.compile("StyledPriceLabel"))  # Adjust this to match the correct class/tag
        
        pattern = r'\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
        
        awa = []
        for element in price:
            # Search for the price using regex on the element's text
            price = re.search(pattern, element.text)
            if price:
                # Print the price if a match is found
                awa.append("$"+price.group())
        try:
            meow = set(awa)
        except:
            meow = [":("]
        pricelist.append(meow)
    else:
        productList.append("cant find ;-;")
        
for productList, pricelist in zip(productList, pricelist):
    wawa.append([productList, ", ".join(pricelist)])
print(tabulate(wawa, headers=["Name", "Price"], tablefmt="pretty"))