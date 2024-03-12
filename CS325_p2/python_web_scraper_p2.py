from bs4 import BeautifulSoup
import requests

def main():

    # Opens the file 'Weblinks' and adds the weblinks to the array
    file = open("Weblinks.txt", "r")
    webArray = (file.read()).split(",")
    # Removes the lasst index that has nothing in it
    webArray.pop()
    
    # Loops through the webArray, scraping the data in them and outputs them into a text file:
    for i, link in enumerate(webArray):
        # Get request for the html in the webpage
        webpage = requests.get(link)

        # Utilizing beautiful soup, we create an html parser 
        soup = BeautifulSoup(webpage.text, "html.parser")
        # It goes into a div and accesses the information in the id where it equals "article-body"
        paragraphs = soup.findAll('div', attrs={"id":"article-body"})
        # Opens the file Article[i+1] to write the data, i is the iteration of the loop
        file1 = open("Article" + str(i + 1), "w")

        # Adds the paragraph data to the text file
        for paragraph in paragraphs:
            file1.write(str(paragraph.text))
        
        # Closes the file
        file1.close()

        # Removes all of the useless indents:
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