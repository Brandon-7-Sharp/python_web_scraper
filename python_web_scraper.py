from bs4 import BeautifulSoup
import requests

def main():

    webArray = ["https://www.space.com/40547-spacex-rocket-evolution.html", 
                "https://www.space.com/nasa-satellite-aurora-infrared-light-photo", 
                "https://www.space.com/16970-cancer-constellation.html",
                "https://www.space.com/nasa-loses-contact-ingenuity-mars-helicopter",
                "https://www.space.com/universe-younger-than-thought-galaxy-motion"]
    
    for i, link in enumerate(webArray):
        webpage = requests.get(link)

        soup = BeautifulSoup(webpage.text, "html.parser")
        title = soup.findAll('div', attrs={"class":"news-article"})
        paragraphs = soup.findAll('div', attrs={"id":"article-body"})
        file1 = open("Article" + str(i + 1), "w")

        for t in title:
            file1.write(str(t.text))

        for paragraph in paragraphs:
            file1.write(str(paragraph.text))
        
        file1.close()

        result = ""
        with open("Article" + str(i + 1), "r+") as file:
            for line in file:
                if not line.isspace():
                    result += line
            file.seek(0)
            file.write(result)
            
        file1.close()


if __name__ == "__main__":
    main()