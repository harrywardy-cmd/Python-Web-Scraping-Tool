from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

element_list = []

options = webdiver.ChomeOptions()
options.add_arument("--headless")
options.add_arument("--no--sandbox")
options.add_arument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())

for page in range(1,3):
    driver = webdriver.Chrome(service=service, options=options)

    url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=%7Bpage%7D"

    driver.get(url)
    time.sleep(2)

    titles = driver.find_elements(By.CLASS_NAME, "title")
    prices = driver.find_elements(By.CLASS_NAME,"price")
    descriptions = driver.find_elements(By.CLASS_NAME,"description")
    ratings = driver.find_elements(By.CLASS_NAME,"ratings")


for i in range(len(titles)):
    element_list.append([
        titles[i].text,
        prices[i].text,
        descriptions[i].text,
        ratings[i].text
    ])

driver.quit()


# Display data

for row in element_list:
    print(row)