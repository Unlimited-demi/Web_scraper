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
    
   
import requests

from bs4 import BeautifulSoup

import os

def scrape_data(url, element_type, amount):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    elements = soup.find_all(element_type)[:amount]

    for index, element in enumerate(elements):

        if element_type == "img":

            # Scraping images

            image_url = element["src"]

            save_image(image_url, index)

        elif element_type == "a":

            # Scraping text files

            file_url = element["href"]

            save_text_file(file_url, index)

def save_image(image_url, index):

    response = requests.get(image_url)

    if response.status_code == 200:

        with open(f"image_{index}.jpg", "wb") as file:

            file.write(response.content)

        print(f"Image {index}.jpg saved successfully.")

def save_text_file(file_url, index):

    response = requests.get(file_url)

    if response.status_code == 200:

        file_name = file_url.split("/")[-1]

        with open(file_name, "w") as file:

            file.write(response.text)

        print(f"Text file {file_name} saved successfully.")

if __name__ == "__main__":

    url = input("Enter the URL to scrape: ")

    element_type = input("Enter the element type to scrape (img/a): ")

    amount = int(input("Enter the amount of data to scrape: "))

    scrape_data(url, element_type, amount)
