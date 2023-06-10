import requests 
from bs4 import BeautifulSoup


print("BBC HEADLINES THIS HOUR \n" *3 + "================\n" *2)

def scrape_headlines():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all("h3" )
    for headline in headlines:
        print(headline.text.strip())



        
if __name__ == "__main__":
    scrape_headlines()
    
   
