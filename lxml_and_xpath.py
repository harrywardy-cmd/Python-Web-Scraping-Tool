from lxml import html
import requests

url = 'https://example.com/'

response = requests.get(url)
tree = html.formstring(response.content)

link_titles = tree.xpath('//a/text()')

for title in link_titles:
    print(title)