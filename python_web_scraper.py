from bs4 import BeautifulSoup
import requests

def main():

    # Creates an array of weblinks that will be looped through
    webArray = ["https://www.space.com/40547-spacex-rocket-evolution.html", 
                "https://www.space.com/nasa-satellite-aurora-infrared-light-photo", 
                "https://www.space.com/16970-cancer-constellation.html",
                "https://www.space.com/nasa-loses-contact-ingenuity-mars-helicopter",
                "https://www.space.com/universe-younger-than-thought-galaxy-motion"]
    
    # Loops through the webArray, scraping the data in them and outputs them into a text file
    for i, link in enumerate(webArray):
        # Get request for the html in the webpage
        webpage = requests.get(link)

        # Utilizing beautiful soup, we create an html parser that goes into 'div' and into each class = "news-article"
        soup = BeautifulSoup(webpage.text, "html.parser")
        title = soup.findAll('div', attrs={"class":"news-article"})
        # Then it goes into another div and access the information in the id where it equals "article-body"
        paragraphs = soup.findAll('div', attrs={"id":"article-body"})
        # Opens the file Article[i] to write the data, i is the iteration of the loop
        file1 = open("Article" + str(i + 1), "w")

        # Adds the title data to the text file
        for t in title:
            file1.write(str(t.text))

        # Adds the paragraph data to the text file
        for paragraph in paragraphs:
            file1.write(str(paragraph.text))
        
        # Closes the file
        file1.close()

        # Removes all of the useless indents
        result = ""
        # Opens the Article and gives permission to read and write to it
        with open("Article" + str(i + 1), "r+") as file:
            # For each line in the file, the useless indents are removed
            for line in file:
                if not line.isspace():
                    result += line
            # Returns the current position in the file back to the beginning
            file.seek(0)
            # Writes the data to the file
            file.write(result)
        # Closes the file
        file1.close()


if __name__ == "__main__":
    main()