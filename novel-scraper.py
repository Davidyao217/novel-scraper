import requests
from bs4 import BeautifulSoup
import os

#https://products.aspose.com/words/python-net/conversion/txt-to-epub/

def main():
    baseURL = "https://freewebnovel.com/blood-warlock-succubus-partner-in-the-apocalypse-novel/chapter-"#Important: Base url: remove chapter number and ".html"
        #"https://freewebnovel.com/unparalleled-after-ten-consecutive-draws/chapter-" 
    novelName = "Blood-Warlock-In-The-Apocalypse" #Important: Novel title used for directory+file name

    chapterCounter = userInputPlez("Please enter starting chapter: ")
    chapterRange = userInputPlez("Please enter how many chapters you want: ")  
    fileName = fileNameGenerator(novelName,chapterCounter, chapterRange)

    scrapingAndWritingToTextFile(fileName, chapterRange, chapterCounter, baseURL)

#this function prompts user input until valid
def userInputPlez(prompt):
    while True:
        try:
            inpt = int(input(prompt))
        except ValueError:
            print("Invalid input")
            continue
        else:
            return inpt

#this function will generate a seperate folder within the text-files folder for this new novel
def fileNameGenerator(novelName, chapterCounter, chapterRange):
    try: 
        os.mkdir("text-files/")
    except:
        pass
    try:
        os.mkdir("text-files/" + novelName)
    except:
        print("\n"+"A folder for this novel already exists in the text-files folder")
    fileName = "text-files/" + novelName+"/" + novelName+ "_Ch:" + str(chapterCounter) + "-" + str(chapterCounter+chapterRange-1) + ".txt"
    return fileName;

def scrapingAndWritingToTextFile(fileName, chapterRange, chapterCounter, baseURL):
    print("\n"+ "Following will indicate which chapter is being scraped: ")
    textfile = open(fileName, "w")
    for x in range(chapterRange): 
            URL = baseURL + str(chapterCounter) + ".html"
            print(chapterCounter)
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