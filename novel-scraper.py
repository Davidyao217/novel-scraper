#Python program to scrape website
#and save quotes from website
from email.mime import base
import requests
from bs4 import BeautifulSoup
import csv

baseURL = "https://freewebnovel.com/unparalleled-after-ten-consecutive-draws/chapter-" #important: Base url: remove chapter number and ".html"

chapterCounter = 323 #Important: Starting Chapter

textfile = open("text-files/a_file.txt", "w")
for x in range(5): #Important: Number of chapters
        URL = baseURL + str(chapterCounter) + ".html"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all('p')
        for element in results:
            textfile.write(element.get_text() + "\n")
        chapterCounter+=1
        textfile.write("\n" + "\n")
textfile.close()

