# Example of how to use BeautifulSoup to identify and extract specific html elements, in this case headings and links

import requests
from bs4 import BeautifulSoup

# Target URL
url = 'https://www.fangraphs.com/leaders/major-league'

# Fetch webpage content
try:
    response = requests.get(url)
    response.raise_for_status() #Checks for HTTP errors
except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
else:
    # Parse html
    soup = BeautifulSoup(response.content, 'html.parser')

headings = soup.find_all('h1')

for heading in headings:
    print(heading.text.strip()) # removes any additional whitespace

links = soup.find_all('a')

for link in links:
    href = link.get('href')
    if href: # Verifies link has valid 'href'
        print(href)

# Example of using BeautifulSoup to perform data analysis on sports data

# import requests                #commented out as the import is already performed in the example above
# from bs4 import BeautifulSoup  #commented out as the import is already performed in the example above

# Target URL
url = 'https://www.fangraphs.com/leaders/major-league'

# Fetch webpage content
try:
    response = requests.get(url)
    response.raise_for_status() #Checks for HTTP errors
except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
else:
    # Parse html
    soup = BeautifulSoup(response.content, 'html.parser')

sports = soup.find_all('div', class_="leaders-major_leaders-major__table__hcmbm") # note the use of double underscore around 'table' (__table__)

for sport in sports:
    player = sport.find('td', class_='align-left fixed').text.strip()  # extracts player name
    games_played = sport.find('td', class_='align-right').text.strip()  # extracts games played
    print(f"Player: {player}, Games Played: {games_played}\n")