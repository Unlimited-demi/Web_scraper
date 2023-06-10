import requests
from bs4 import BeautifulSoup
import os
import base64

def scrape_images(url, num_images):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    img_tags = soup.find_all("img")

    image_urls = []
    for img in img_tags:
        if img.has_attr("src"):
            image_urls.append(img["src"])

    for i, img_url in enumerate(image_urls[:num_images]):
        if img_url.startswith("data:image/"):
            save_base64_image(img_url, i)
        else:
            save_image(img_url, i)

def save_image(image_url, index):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(f"image_{index}.jpg", "wb") as file:
            file.write(response.content)
        print(f"Image {index}.jpg saved successfully.")

def save_base64_image(base64_data, index):
    _, data = base64_data.split(",", 1)
    image_data = base64.b64decode(data)
    with open(f"image_{index}.jpg", "wb") as file:
        file.write(image_data)
    print(f"Base64 image {index}.jpg saved successfully.")

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    num_images = int(input("Enter the number of images to scrape: "))

    scrape_images(url, num_images)
