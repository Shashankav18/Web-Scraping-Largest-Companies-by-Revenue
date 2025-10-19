import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the first table
table = soup.find("table", {"class": "wikitable"})
df = pd.read_html(str(table))[0]

# Save to CSV
df.to_csv("data/largest_companies.csv", index=False)
print("✅ Data scraped and saved to data/largest_companies.csv")
