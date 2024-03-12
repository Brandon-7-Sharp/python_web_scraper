######################################################################################
#
# FileScraper:
#   Class located in the refine_data.py file
#   Main task is using Beautiful Soup to grab only the paragraph data from the raw HTML
#       stored in the RawArticle# for each article. This refined data is then returned.
#
# WriteData:
#   Class located in the refine_data.py file
#   Main task is writing the refined data to a processedArticle# for each article's data
#
######################################################################################


import os
from bs4 import BeautifulSoup

# Class for refining the data that was obtained in the get_data
class FileScraper:
    # Method that reads the raw html in the rawArticle[i] file and uses BeautifulSoup to grab only the paragraphs of the webpage
    def scrape_data(self, i: int, path_raw: str) -> str:
        # Opens the file that has the raw data for the specified article
        fileToReadRaw = open(str(os.path.dirname(os.path.dirname(__file__))) + path_raw + str(i + 1))
        # Utilizing beautiful soup, we create an html parser 
        soup = BeautifulSoup(fileToReadRaw, "html.parser")
        # It goes into a div and accesses the information in the id where it equals "article-body" and stores that data in the paragraphs string
        paragraphs: str = soup.findAll('div', attrs={"id":"article-body"})
        # Returns a string will all the paragraph in
        return paragraphs
    
# Class for writing the refined data to a specified file
class WriteData:
    # Method that writes the refined data(gives as paragraphs variable) to the specified file
    def write_data(self, paragraphs: str, i: int, path_pro: str) -> None:
        # Finds the path for the specified file
        file_to_read_pro: str = str(os.path.dirname(os.path.dirname(__file__))) + path_pro + str(i+1)
        # Opens the file to be written to
        file1 = open(file_to_read_pro, "w")
        # Loops through the paragraphs in the paragraphs variable and writes them to the file
        for paragraph in paragraphs:
            file1.write(str(paragraph.text))
        # Closes the file
        file1.close()




# # Class that 
# class FileReader:
#     def __init__(self, filename) -> None:
#         self.filename = filename

#     def read_web_links(self) -> typing.List[str]:
#         with open(self.filename, "r") as file:
#             web_links: list[str] = file.read().split(",")
#             web_links.pop()
#         return web_links


# fileToReadPro = str(os.path.dirname(os.path.dirname(__file__))) + "/Data/processed/rawArticle" + str(i + 1)
# Opens the file Article[i+1] to write the data, i is the iteration of the loop

# def main():
#     weblink_reader = WebLinkReader("Weblinks.txt")
#     web_links: list[str] = weblink_reader.read_web_links()

#     web_scraper = WebScraper()
#     writer = WriteData()
#     for i, link in enumerate(web_links):
#          writer.write_data(web_scraper, link, i)


# if __name__ == "__main__":
#     main()




# # Opens the file 'Weblinks' and adds the weblinks to the array
# file = open("Weblinks.txt", "r")
# webArray = (file.read()).split(",")
# # Removes the lasst index that has nothing in it
# webArray.pop()


# # Loops through the webArray, scraping the data in them and outputs them into a text file:
# for i, link in enumerate(webArray):
#     # Get request for the html in the webpage
#     # webpage = requests.get(link)

#     fileToReadRaw = open(str(os.path.dirname(os.path.dirname(__file__))) + "/Data/raw/rawArticle" + str(i + 1))
#     # Utilizing beautiful soup, we create an html parser 
#     soup = BeautifulSoup(fileToReadRaw, "html.parser")
#     # It goes into a div and accesses the information in the id where it equals "article-body"
#     paragraphs = soup.findAll('div', attrs={"id":"article-body"})

#     fileToReadPro = str(os.path.dirname(os.path.dirname(__file__))) + "/Data/processed/rawArticle" + str(i + 1)
#     # Opens the file Article[i+1] to write the data, i is the iteration of the loop
#     file1 = open(fileToReadPro, "w")

#     # Adds the paragraph data to the text file
#     for paragraph in paragraphs:
#         file1.write(str(paragraph.text))
    
#     # Closes the file
#     file1.close()

#     # # Removes all of the useless indents:
#     # result = ""
#     # # Opens the Article and gives permission to read and write to it
#     # with open("Article" + str(i + 1), "r+") as file:
#     #     # For each line in the file, the useless indents are removed
#     #     for line in file:
#     #         if not line.isspace():
#     #             result += line
#     #     # Returns the current position in the file back to the beginning
#     #     file.seek(0)
#     #     # Writes the data to the file
#     #     file.write(result)
#     # # Closes the file
#     # file1.close()