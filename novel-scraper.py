import requests
from bs4 import BeautifulSoup
import os

def main():
    baseURL = "https://freewebnovel.com/unparalleled-after-ten-consecutive-draws/chapter-" #Important: Base url: remove chapter number and ".html"

    chapterCounter = 323 #Important: Starting Chapter
    chapterRange = 2 #Important: Number of chapters
    novelName = "Unparalleled-after-ten-consecutive-draws" #Important: Novel title used for directory+file name
    fileName = fileNameGenerator(novelName,chapterCounter, chapterRange, )

    scrapingAndWritingToTextFile(fileName, chapterRange, chapterCounter, baseURL)

#this function will generate a seperate folder within the text-files folder for this new novel
def fileNameGenerator(novelName, chapterCounter, chapterRange):
    try:
        os.mkdir("text-files/" + novelName)
    except:
        print("A folder for this novel already exists in the text-files folder")
    fileName = "text-files/" + novelName+"/" + novelName+ "_Ch:" + str(chapterCounter) + "-" + str(chapterCounter+chapterRange-1) + ".txt"
    return fileName;

def scrapingAndWritingToTextFile(fileName, chapterRange, chapterCounter, baseURL):
    textfile = open(fileName, "w")
    for x in range(chapterRange): 
            URL = baseURL + str(chapterCounter) + ".html"
            print(URL)
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find_all('p')
            for element in results:
                textfile.write(element.get_text() + "\n")
            chapterCounter+=1
            textfile.write("\n" + "\n")
    textfile.close()

if __name__ == '__main__':
    main()