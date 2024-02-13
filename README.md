# Python Web Scraper
## Description
This python program scrapes 5 Space related web pages for their information. It will not scrape ads, comments, or any other useless information.

## Getting Started
First, you need to install two packages, beautifulsoup4 and requests

```
pip install beautifulsoup4
```
```
pip install requests
```

Next, you need to create a new enviroment with the requirements.yaml provided in this repo.

In the CMD, go to the location where you have this repo in your computer.

Then, create a new enviroment from the requirements.yaml provided in this repo, where my_yaml_env_name is the name you create for your enviroment.
```
conda create --name my_yaml_env_name --file requirements.yaml
```
Then make sure the enviroment is activated by typing the below code in the same location in the cmd, where my_yaml_env_name is the name you create for your enviroment.
```
git activate my_yaml_env_name
```

## Explanation
Imports beautifulsoup4 from bs4 and imports requests
```
from bs4 import BeautifulSoup
import requests
```
Uses requests to send an HTML get requests for the contents of the specified webpage
```
webpage = requests.get("https://www.space.com/40547-spacex-rocket-evolution.html")
```
Creates a parse tree to extract data from HTML and sets it to soup
```
soup = BeautifulSoup(webpage.text, "html.parser")
```
Looks through the HTML to find all the info in div tags where id=article-body
```
paragraphs = soup.findAll('div', attrs={"id":"article-body"})
```

Loops through the title and paragraph HTML information scraped and outputs it
```
for t in title:
    print(t.text)

for paragraph in paragraphs:
    print(paragraph.text)
```

## Output
The program will output 5 text files called Article1 - Article5.

Each one will have a different article in them.