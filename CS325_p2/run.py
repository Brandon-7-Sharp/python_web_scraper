######################################################################################
#
# In this program there are 4 main classes(and the main function in this file).
#   1) WebLinkReader
#   2) WebScraper
#   3) FIleScraper
#   4) WriteData
#
# WebLinkReader:
#   Class located in the get_data.py file
#   Main task for this class is to read the weblinks stored in the Weblinks.txt file and 
#       write the strings to an array, which it returns.
#
# WebScraper:
#   Class located in the get_data.py file
#   Main task is going to the websites stored in the webArray, and writing their raw HTML
#       data to individual files labeled RawArticle# in the Data->Raw directory
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
#
# Customizability:
#   Users can change the paths of where the raw data is stored
#   Users can change the paths of where the refined data is stored
#   Users can change the path of where the Weblinks.txt file is located
#
# SOLID Principles:
#   S = Each of my classes does a specific task, as explained above. 
#       Each method in the classes also does one specific task. For example, the read_web_links 
#       method in the WebLinkReader class only reaads the weblinks in the Weblinks.txt and returns 
#       their data
#   O = New Classes can be added and the program would still function. Say that you wanted 
#       to add a class that formats the text that will be stored in the refined data txt file,
#       you can easily add a new class and function that will be used before the data will be written 
#       to the refined data txt file
#   L = Being that I assigned tasks individually to classes and functions, if the user implements
#       a new class that wil inherit a class that I created, the new class will not be forced to 
#       implement several useless methods
#   I = I do not enforce children of my classes to implement methods from their parent, so creating
#       a new class and implementing a parent class will not cause any issues or foce the child
#       to implement mehtods that it will not need   
#   D = My code does not have dependencies from low level modules on high level modyles beacuse none 
#       of my variables are hard coded. Each variable is only depended on the level it is in
#       
#
######################################################################################


import module_1.get_data as gd
import module_2.refine_data as rd

def main():

    # Can change the directories to what user wants
    path_for_RAW = "/Data/raw/RawArticle"
    path_for_PROCESSED = "/Data/processed/processedArticle"


    # From Module 1 folder, get_data file: Creates a WebLinkReader object to store the location of the Weblinks file
    web_link = gd.WebLinkReader("Weblinks.txt")

    # From Module 1 folder, get_data file: Calls the read_web_links method of the WebLinkReader class to 
    # return an array of the weblinks that are in the Weblinks text file
    webArray: list[str] = web_link.read_web_links()

    # From Module 1 folder, get_data file: Creates a WebScrapper object
    web_scraper_r = gd.WebScraper()

    # Loops through the webArray, scraping the data in them and outputs them into a text file:
    # For every web link the the webArray, it sends the address to the scrape_data method of the WebScraper class
    for i, link in enumerate(webArray):
        # From Module 1 folder, get_data file: Sends in the weblink address and the index to append to the end of the file name
        web_scraper_r.scrape_data(link, i, path_for_RAW)
    
    # # From Module 2 folder, refine_data file: Creates objects from the FileScraper and WriteData classes
    web_scraper_p = rd.FileScraper()
    writer = rd.WriteData()

    # Loops however many weblinks there are
    for i, link in enumerate(webArray):
         paragraphs: str = web_scraper_p.scrape_data(i, path_for_RAW)
         # From Module 2 folder, refine_data file: Calls the write_data method, sending in the FileScraper object and the 
         # index to append to the end of the file name
         writer.write_data(paragraphs, i, path_for_PROCESSED)


if __name__ == "__main__":
    main()
