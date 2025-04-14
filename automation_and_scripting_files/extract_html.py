from bs4 import BeautifulSoup

html_content = """
<div class="product">
    <h1>Awesome Headphones</h1>
    <p class = "price">$99.99</p>
    <p class = "description">These headphones offer amazing sound quality!</p>
</div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

product_header_tag = soup.find('h1')
product_name = product_header_tag.get_text()

price_tag = soup.find('p', class_="price")
price = price_tag.get_text()

description_tag = soup.find('p', class_="description")
description = description_tag.get_text()

print(f"Product name: {product_name}")
print(f"Price: {price}")
print(f"Description: {description}")