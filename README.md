# Python Web Scraper
## Description
This python program scrapes 5 Space related web pages for their information. It will not scrape ads, comments, or any other useless information.

## Getting Started
First, you need to create a new enviroment with the requirements.yaml provided in this repo.

In the CMD, go to the location where you have this repo in your computer.

Then, create a new enviroment from the requirements.yaml provided in this repo, where my_yaml_env_name is the name you create for your enviroment.
```
conda create --name my_yaml_env_name --file requirements.yaml
```
Then make sure the enviroment is activated by typing the below code in the same location in the cmd, where my_yaml_env_name is the name you create for your enviroment.
```
git activate my_yaml_env_name
```

## run.py Explanation:




## get_data.py Explanation:

### Imports:
Imports os and requests.
```
import os
import requests
```

### Classes:
WebLinkReader Class: Has the '__init__(self, path: str) -> None' method that initializes each Object with the path of where the 'Weblinks.txt' is located. Has the 'read_web_links(self)' function that only takes in intself. The function opens the 'Weblinks.txt' file, reads the contents into an array, slitting the indexes by the commas between web addresses, and returns that array of web addresses.

WebScraper Class: Has the 'scrape_data(self, link: str, i: int, path_raw: str) -> None' function that takes in an object of WebScraper (self), the web address for a particular website (link), the index of which web address this is (i), and the path for where the raw txt files are stored (path_raw). The function uses the requests module to obtain the html of the specified web address, then opens the file path to where the raw data is going to be stored, iterates through a for loop inserting the data into the file, and finally closes the file.

## refine_data.py Explanation:

### Imports:
Imports os and beautifulsoup4 from bs4.
```
import os
from bs4 import BeautifulSoup
```

### Classes:
FileScraper Class: Has the function 'scrape_data(self, i: int, path_raw: str) -> str' that takes in an instance of the FileScraper class (self) and the index of which raw data text file (path_raw). It first opens the raw data file (path given from parameters), then it uses BeautifulSoup to parse the html in that file by using the BeautifulSoup function 'findAll('div', attrs={"id":"article-body"})' where in a div tag there is an id set to 'article-body'. It then returns all of that information as a string.

WriteData Class: Has the function 'write_data(self, paragraphs: str, i: int, path_pro: str) -> None' that takes in an instance of the WriteData class (self), a string with all of the processed data (paragraphs), the index of which processed data text file (i), and the path from where run.py is to the file wehre it will write to (path_raw). It first creates the full path of the file it will write the processed data to, then it opens that file and goes through a for loop writing the paragraphs into the processed text file, closing it afterwards.

## summarize_data.py

### Imports:
Imports os
```
import os
```

### Classes:
WriteSummarized Class: Has the function 'write_summarized(self, paragraphs: str, i: int, path_pro: str) -> None' that takes in an instance of WriteSummarized (self), the data in the processed text file (paragraphs), the index of which processed text file is being used (i), and the path to where the summarized data will be written to. It first creates the full path to the file it will write the summarized data to, opens that file, iterates through a for loop writing the summarized paraghraph and title created by open ai, and finally closes the file.


Uses requests to send an HTML get requests for the contents of the specified webpage.
```
webpage = requests.get("https://www.space.com/40547-spacex-rocket-evolution.html")
```
Creates a parse tree to extract data from HTML and sets it to soup.
```
soup = BeautifulSoup(webpage.text, "html.parser")
```
Looks through the HTML to find all the info in div tags where id=article-body
```
paragraphs = soup.findAll('div', attrs={"id":"article-body"})
```


## Output
The program will output 30 text files (10 with the raw html, 10 with the processed data that is readable, and 10 with summarized data by open ai) based on 10 different websites
