# Importing requests and BeautifulSoup
import requests
from bs4 import BeautifulSoup

x = int(input("Where to start from: "))

#   TASK: write code to scrape last page number

for pageNumber in range(x,25073):

    # Opening the file to which the scraped data is written
    #   - Use absolute path (relative path was not writing to the real file)
    file1 = open(r"<ABSOLUTE PATH>\headlines.txt","a",encoding="utf-8")
    
    # URL for the archive page - replace if necessary in future
    url = "https://indianexpress.com/section/news-archive/page/"+str(pageNumber)+"/"

    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data,"html.parser")

    # Filters by the tags needed to scrape the headline
    for divtag in soup.find_all('h2', {'class': 'title'}):
        for atag in divtag.find_all('a'):

            #HEADLINES
            hl=atag.get_text()
            print("Headline: ",hl)

            # Writes the lowercase headline to the file
            file1.write(hl.lower())
            file1.write("\n")

            # URL for the article 
            # print("URL: ",atag["href"])
            
            print("")

    # Printing the indicator during script run
    print(">> PART ",pageNumber," DONE")
    
    #Closes file every cycle to prevent data loss
    file1.close()